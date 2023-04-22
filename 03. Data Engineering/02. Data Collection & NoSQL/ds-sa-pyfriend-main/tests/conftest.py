import os
import pytest
from string import Template

pytest.RESOURCE_PATH = os.path.join(os.getcwd(), 'tests', 'resources')

@pytest.fixture(autouse=True, scope="module")
def setup_teardown_msg():
    template = Template("""
        -------------------------------------
        $msg...
        -------------------------------------
        """)
    yield print(template.substitute(msg="Setting up"))
    print(template.substitute(msg="Tearing down"))


