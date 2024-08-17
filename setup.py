from setuptools import Extension, setup


def main():
    setup(
        ext_modules=[
            Extension(
                name="fputs",
                sources=["fputsmodule.c"],
            )
        ]
    )


if __name__ == "__main__":
    main()
