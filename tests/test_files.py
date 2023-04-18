import os
import pytest
from glogging.glogging import ensure_path_exists


def test_ensure_path_exists_handles_oserror(mocker):
    # Define the directory path to create
    dir_path = "test_directory"
    path = os.path.join(dir_path, "dummy_file")

    # Mock os.makedirs to raise OSError after the first call
    mock_makedirs = mocker.patch("os.makedirs", side_effect=[None, None])

    # Call the ensure_path_exists function twice
    ensure_path_exists(path)
    ensure_path_exists(path)

    # Check if the mock was called twice with the correct arguments
    assert mock_makedirs.call_count == 2
    mock_makedirs.assert_called_with(dir_path)
