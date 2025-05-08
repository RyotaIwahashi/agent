"""Tests for the agent module."""

import pytest
from unittest.mock import MagicMock, patch

from src.agent import extract_content


def test_extract_content():
    """Test that content is correctly extracted from an API response."""
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = "Test content"
    
    result = extract_content(mock_response)
    assert result == "Test content"
