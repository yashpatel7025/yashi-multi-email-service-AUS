import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="multi-email-service-yashpatel-AUS",
    version="1.0.0",
    author="Yash Patel",
    author_email="yashwadia7025@gmail.com",
    description="package to send email using Amazon SES, Google SMTP and SendGrid",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yashpatel7025/yashi-multi-email-service-AUS",
    install_requires=[ "sendgrid == 6.7.1"],
    project_urls={
        "Bug Tracker": "https://github.com/yashpatel7025/yashi-multi-email-service-AUS/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)