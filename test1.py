import pytest
from Random_Forest_SCD import predict_ids  # Import the function you want to test

# Pytest Fixture to set up the environment
@pytest.fixture
def setup_environment():
    # You might want to set up your environment here
    # For example, initializing the Anvil server or loading the model
    yield
    # Clean up the environment after the tests, if necessary

# Pytest for Testing IDS against Input
def test_ids_against_input(setup_environment):
    # Step 1: Access the IDS Dashboard
    # (Assuming you have a way to access the IDS dashboard)

    # Step 2: Identify the Packet Input Section
    # (Assuming you have identified where packet inputs can be configured)

    # Step 3: Send Normal Packet
    normal_result = predict_ids(duration=1, src_bytes=100, dst_bytes=200, count=10, srv_count=5)

    # Step 4: Check IDS Result
    # IDS should accurately identify the normal packet
    assert normal_result == "Normal"

    # Step 5: Send Malicious Packet
    malicious_result = predict_ids(duration=0, src_bytes=10000, dst_bytes=20000, count=1000, srv_count=500)

    # Step 6: Check IDS Result
    # IDS should accurately identify the malicious packet
    assert malicious_result == "Malicious"
