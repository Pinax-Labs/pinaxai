"""
Agno Tracing Module

This module provides OpenTelemetry-based tracing capabilities for Agno agents.
It uses the openinference-instrumentation-agno package for automatic instrumentation
and provides a custom DatabaseSpanExporter to store traces in the Agno database.
"""

from pinaxai.tracing.exporter import DatabaseSpanExporter
from pinaxai.tracing.setup import setup_tracing

__all__ = ["DatabaseSpanExporter", "setup_tracing"]
