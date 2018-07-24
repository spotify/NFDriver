#!/usr/bin/env python

import sys

from nfbuildosx import NFBuildOSX


def main():
    library_target = 'NFDriver'
    nfbuild = NFBuildOSX()
    nfbuild.build_print("Installing Dependencies")
    nfbuild.installDependencies(android=True)
    # Make our main build artifacts
    nfbuild.build_print("C++ Build Start (x86)")
    nfbuild.makeBuildDirectory()
    nfbuild.generateProject(android=True, android_arm=False)
    targets = [library_target]
    for target in targets:
        nfbuild.buildTarget(target)
    nfbuild.build_print("C++ Build Start (arm64)")
    nfbuild.makeBuildDirectory()
    nfbuild.generateProject(android=False, android_arm=True)
    targets = [library_target]
    for target in targets:
        nfbuild.buildTarget(target)
    nfbuild.buildGradle()


if __name__ == "__main__":
    main()
