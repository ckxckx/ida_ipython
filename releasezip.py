import os
import sys
import zipfile
import shutil

import generate_kernels


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def create_release_directory():
    if os.path.exists('release'):
        shutil.rmtree('release')
    os.makedirs('release/notebook-kernels')
    generate_kernels.generate_kernels('release/notebook-kernels')
    shutil.copy('plugin/ida_ipython.py', 'release/ida_ipython.py')
    shutil.copy('README.md', 'release/README.md')
    shutil.copy('LICENSE', 'release/LICENSE')


def main(version):
    create_release_directory()

    with zipfile.ZipFile('release-{}.zip'.format(version), 'w') as release:
        zipdir('release', release)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print "No release name provided"
