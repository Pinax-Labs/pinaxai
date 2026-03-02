"""Remote content loaders for Knowledge.

This module provides loaders for various cloud storage providers:
- S3Loader: AWS S3
- GCSLoader: Google Cloud Storage
- SharePointLoader: Microsoft SharePoint
- GitHubLoader: GitHub repositories
- AzureBlobLoader: Azure Blob Storage

All loaders inherit from BaseLoader which provides common utilities for
computing content names, creating content entries, and merging metadata.
"""

from pinaxai.knowledge.loaders.azure_blob import AzureBlobLoader
from pinaxai.knowledge.loaders.base import BaseLoader, FileToProcess
from pinaxai.knowledge.loaders.gcs import GCSLoader
from pinaxai.knowledge.loaders.github import GitHubLoader
from pinaxai.knowledge.loaders.s3 import S3Loader
from pinaxai.knowledge.loaders.sharepoint import SharePointLoader

__all__ = [
    "BaseLoader",
    "FileToProcess",
    "S3Loader",
    "GCSLoader",
    "SharePointLoader",
    "GitHubLoader",
    "AzureBlobLoader",
]
