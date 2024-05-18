from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit-ai-assist",
    version="0.1.0",
    author="Kaitlyn Hennacy",
    author_email="kaitlynhennacy@gmail.com",
    description="A built in data analyst for your Streamlit app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=["streamlit>=1.2", "jinja2", "plotly", "replicate", "transformers", "pydantic", "requests", "sqlalchemy==1.4", "snowflake-sqlalchemy", "snowflake-snowpark-python"],
)
