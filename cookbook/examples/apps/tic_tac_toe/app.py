import nest_asyncio
import streamlit as st
from agents import get_tic_tac_toe_players
from pinaxai.utils.log import logger
from utils import (
    CUSTOM_CSS,
    TicTacToeBoard,
    display_board,
    display_move_history,
    show_agent_status,
)

nest_asyncio.apply()

# Page configuration
st.set_page_config(
    page_title="Agent Tic Tac Toe",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load custom CSS with dark mode support
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def main():
    ####################################################################
    # App header
    ####################################################################
    st.markdown(
        "<h1 class='main-title'>Agents play Tic Tac Toe</h1>",
        unsafe_allow_html=True,
    )

    ####################################################################
    # Initialize session state
    ####################################################################
    if "game_started" not in st.session_state:
        st.session_state.game_started = False
        st.session_state.game_paused = False
        st.session_state.move_history = []

    with st.sidebar:
        st.markdown("### Game Controls")
        model_options = {
            "gpt-4o": "openai:gpt-4o",
            "gpt-4o-mini": "openai:gpt-4o-mini",
            "gpt-4.5": "openai:gpt-4.5-preview",
            "o1-pro": "openai:o1-pro",
            "o3-mini": "openai:o3-mini",
            "claude-3.5": "anthropic:claude-3-5-sonnet",
            "claude-3.7": "anthropic:claude-3-7-sonnet",
            "claude-3.7-thinking": "anthropic:claude-3-7-sonnet-thinking",
            "gemini-pro": "google:gemini-2.5-pro-exp-03-25",
            "gemini-flash": "google:gemini-2.0-flash",
            "llama-3.3": "groq:llama-3.3-70b-versatile",
        }
        ################################################################
        # Model selection
        ################################################################
        selected_p_x = st.selectbox(
            "Select Player X",
            list(model_options.keys()),
            index=list(model_options.keys()).index("gpt-4.5"),
            key="model_p1",
        )
        selected_p_o = st.selectbox(
            "Select Player O",
            list(model_options.keys()),
            index=list(model_options.keys()).index("claude-3.7"),
            key="model_p2",
        )

        ################################################################
        # Game controls
        ################################################################
        col1, col2 = st.columns(2)
        with col1:
            if not st.session_state.game_started:
                if st.button("▶️ Start Game"):
                    st.session_state.player_x, st.session_state.player_o = (
                        get_tic_tac_toe_players(
                            model_x=model_options[selected_p_x],
                            model_o=model_options[selected_p_o],
                            debug_mode=True,
                        )
                    )
                    st.session_state.game_board = TicTacToeBoard()
                    st.session_state.game_started = True
                    st.session_state.game_paused = False
                    st.session_state.move_history = []
                    st.rerun()
            else:
                game_over, _ = st.session_state.game_board.get_game_state()
                if not game_over:
                    if st.button(
                        "⏸️ Pause" if not st.session_state.game_paused else "▶️ Resume"
                    ):
                        st.session_state.game_paused = not st.session_state.game_paused
                        st.rerun()
        with col2:
            if st.session_state.game_started:
                if st.button("🔄 New Game"):
                    st.session_state.player_x, st.session_state.player_o = (
                        get_tic_tac_toe_players(
                            model_x=model_options[selected_p_x],
                            model_o=model_options[selected_p_o],
                            debug_mode=True,
                        )
                    )
                    st.session_state.game_board = TicTacToeBoard()
                    st.session_state.game_paused = False
                    st.session_state.move_history = []
                    st.rerun()

    ####################################################################
    # Header showing current models
    ####################################################################
    if st.session_state.game_started:
        st.markdown(
            f"<h3 style='color:#87CEEB; text-align:center;'>{selected_p_x} vs {selected_p_o}</h3>",
            unsafe_allow_html=True,
        )

    ####################################################################
    # Main game area
    ####################################################################
    if st.session_state.game_started:
        game_over, status = st.session_state.game_board.get_game_state()

        display_board(st.session_state.game_board)

        # Show game status (winner/draw/current player)
        if game_over:
            winner_player = (
                "X" if "X wins" in status else "O" if "O wins" in status else None
            )
            if winner_player:
                winner_num = "1" if winner_player == "X" else "2"
                winner_model = selected_p_x if winner_player == "X" else selected_p_o
                st.success(f"🏆 Game Over! Player {winner_num} ({winner_model}) wins!")
            else:
                st.info("🤝 Game Over! It's a draw!")
        else:
            # Show current player status
            current_player = st.session_state.game_board.current_player
            player_num = "1" if current_player == "X" else "2"
            current_model_name = selected_p_x if current_player == "X" else selected_p_o

            show_agent_status(
                f"Player {player_num} ({current_model_name})",
                "It's your turn",
            )

        display_move_history()

        if not st.session_state.game_paused and not game_over:
            # Thinking indicator
            st.markdown(
                f"""<div class="thinking-container">
                    <div class="agent-thinking">
                        <div style="margin-right: 10px; display: inline-block;">🔄</div>
                        Player {player_num} ({current_model_name}) is thinking...
                    </div>
                </div>""",
                unsafe_allow_html=True,
            )

            valid_moves = st.session_state.game_board.get_valid_moves()

            current_agent = (
                st.session_state.player_x
                if current_player == "X"
                else st.session_state.player_o
            )
            response = current_agent.run(
                f"""\
Current board state:\n{st.session_state.game_board.get_board_state()}\n
Available valid moves (row, col): {valid_moves}\n
Choose your next move from the valid moves above.
Respond with ONLY two numbers for row and column, e.g. "1 2".""",
                stream=False,
            )

            try:
                import re

                numbers = re.findall(r"\d+", response.content if response else "")
                row, col = map(int, numbers[:2])
                success, message = st.session_state.game_board.make_move(row, col)

                if success:
                    move_number = len(st.session_state.move_history) + 1
                    st.session_state.move_history.append(
                        {
                            "number": move_number,
                            "player": f"Player {player_num} ({current_model_name})",
                            "move": f"{row},{col}",
                        }
                    )

                    logger.info(
                        f"Move {move_number}: Player {player_num} ({current_model_name}) placed at position ({row}, {col})"
                    )
                    logger.info(
                        f"Board state:\n{st.session_state.game_board.get_board_state()}"
                    )

                    # Check game state after move
                    game_over, status = st.session_state.game_board.get_game_state()
                    if game_over:
                        logger.info(f"Game Over - {status}")
                        if "wins" in status:
                            st.success(f"🏆 Game Over! {status}")
                        else:
                            st.info(f"🤝 Game Over! {status}")
                        st.session_state.game_paused = True
                    st.rerun()
                else:
                    logger.error(f"Invalid move attempt: {message}")
                    response = current_agent.run(
                        f"""\
Invalid move: {message}

Current board state:\n{st.session_state.game_board.get_board_state()}\n
Available valid moves (row, col): {valid_moves}\n
Please choose a valid move from the list above.
Respond with ONLY two numbers for row and column, e.g. "1 2".""",
                        stream=False,
                    )
                    st.rerun()

            except Exception as e:
                logger.error(f"Error processing move: {str(e)}")
                st.error(f"Error processing move: {str(e)}")
                st.rerun()
    else:
        st.info("👈 Press 'Start Game' to begin!")

    ####################################################################
    # About section
    ####################################################################
    st.sidebar.markdown(f"""
    ### 🎮 Agent Tic Tac Toe Battle
    Watch two agents compete in real-time!

    **Current Players:**
    * 🔵 Player X: `{selected_p_x}`
    * 🔴 Player O: `{selected_p_o}`

    **How it Works:**
    Each Agent analyzes the board and employs strategic thinking to:
    * 🏆 Find winning moves
    * 🛡️ Block opponent victories
    * ⭐ Control strategic positions
    * 🤔 Plan multiple moves ahead

    Built with Streamlit and Pinaxai
    """)


if __name__ == "__main__":
    main()
