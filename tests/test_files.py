import os
from unittest.mock import MagicMock, patch
from glogging.glogging import ensure_path_exists


def test_ensure_path_exists_works():
    # Define the directory path to create
    dir_path = "test_directory"

    # Mock os.makedirs
    with patch("os.makedirs") as mock_makedirs:
        # Call the os.makedirs with the mock in place
        os.makedirs(dir_path)

        # Check if the mock was called with the correct arguments
        mock_makedirs.assert_called_once_with(dir_path)


def test_ensure_path_exists_handles_oserror():
    # Define the directory path to create
    dir_path = "test_directory"
    path = os.path.join(dir_path, "dummy_file")

    # Mock os.makedirs to raise OSError after the first call
    with patch("os.makedirs", side_effect=[None, None]) as mock_makedirs:
        # Call the ensure_path_exists function twice
        ensure_path_exists(path)
        ensure_path_exists(path)

        # Check if the mock was called twice with the correct arguments
        assert mock_makedirs.call_count == 2
        mock_makedirs.assert_called_with(dir_path)
