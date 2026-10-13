# test_shirtificate.py
import os
from unittest.mock import MagicMock, patch
import pytest
from shirtificate import create_shirtificate, main


@pytest.fixture
def dummy_image(tmp_path):
    """Creates a temporary dummy image so FPDF.image() doesn't fail if running integration tests."""
    from PIL import Image

    img_path = "shirtificate.png"
    if not os.path.exists(img_path):
        img = Image.new("RGB", (600, 600), color="red")
        img.save(img_path)
    yield
    # Cleanup optional: leave or remove depending on your environment


@patch("shirtificate.FPDF")
def test_pdf_configuration_and_methods(mock_fpdf):
    """Test that FPDF is called with correct parameters and methods are triggered."""
    mock_pdf_instance = MagicMock()
    mock_fpdf.return_value = mock_pdf_instance

    create_shirtificate("John Harvard")

    # 1. Verify page was added
    mock_pdf_instance.add_page.assert_called_once()

    # 2. Verify image was placed at the expected coordinates (centered)
    mock_pdf_instance.image.assert_called_once_with(
        "shirtificate.png", x=20, y=60, w=170
    )

    # 3. Verify text color was set to white (255, 255, 255)
    mock_pdf_instance.set_text_color.assert_called_with(255, 255, 255)

    # 4. Verify output was called with correct filename
    mock_pdf_instance.output.assert_called_once_with("shirtificate.pdf")


@patch("shirtificate.FPDF")
def test_correct_name_in_cell(mock_fpdf):
    """Test that the user's name is properly formatted into the text cell."""
    mock_pdf_instance = MagicMock()
    mock_fpdf.return_value = mock_pdf_instance

    test_name = "Alice"
    create_shirtificate(test_name)

    # Inspect all calls to .cell() to ensure "Alice took CS50" was passed
    cell_calls = [
        call[0] for call in mock_pdf_instance.cell.call_args_list
    ]
    all_text_arguments = [
        arg for args_tuple in cell_calls for arg in args_tuple
    ]

    assert "CS50 Shirtificate" in all_text_arguments
    assert f"{test_name} took CS50" in all_text_arguments


@patch("shirtificate.create_shirtificate")
@patch("builtins.input", return_value="David J. Malan")
def test_main_cli_flow(mock_input, mock_create):
    """Test that main() correctly captures CLI input and passes it to create_shirtificate."""
    main()
    mock_input.assert_called_once()
    mock_create.assert_called_once_with("David J. Malan")


def test_integration_pdf_creation(dummy_image):
    """Integration test: Ensure the script actually produces a valid PDF file on disk."""
    output_filename = "shirtificate.pdf"

    # Remove existing file if present before test
    if os.path.exists(output_filename):
        os.remove(output_filename)

    create_shirtificate("Test User")

    # Assert file exists and is not empty
    assert os.path.exists(output_filename)
    assert os.path.getsize(output_filename) > 0