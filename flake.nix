{
  description =
    "A shared kernel used by artifact domains for dealing with changes in source code";
  inputs = rec {
    nixos.url = "github:NixOS/nixpkgs/nixos-23.05";
    flake-utils.url = "github:numtide/flake-utils/v1.0.0";
    pythoneda-base = {
      url = "github:pythoneda/base/0.0.1a16";
      inputs.nixos.follows = "nixos";
      inputs.flake-utils.follows = "flake-utils";
    };
  };
  outputs = inputs:
    with inputs;
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixos { inherit system; };
        pname = "pythoneda-artifact-shared-changes";
        description =
          "A shared kernel used by artifact domains for dealing with changes in source code";
        license = pkgs.lib.licenses.gpl3;
        homepage = "https://github.com/pythoneda-artifact-shared/changes";
        maintainers = with pkgs.lib.maintainers; [ ];
        nixpkgsRelease = "nixos-23.05";
        shared = import ./nix/shared.nix;
        pythonpackage = "pythonedaartifactsharedchanges";
        pythoneda-artifact-shared-changes-for =
          { version, pythoneda-base, python }:
          let
            pythonVersionParts = builtins.splitVersion python.version;
            pythonMajorVersion = builtins.head pythonVersionParts;
            pythonMajorMinorVersion =
              "${pythonMajorVersion}.${builtins.elemAt pythonVersionParts 1}";
            pnameWithUnderscores =
              builtins.replaceStrings [ "-" ] [ "_" ] pname;
            wheelName =
              "${pnameWithUnderscores}-${version}-py${pythonMajorVersion}-none-any.whl";
          in python.pkgs.buildPythonPackage rec {
            inherit pname version;
            projectDir = ./.;
            src = ./.;
            format = "pyproject";

            nativeBuildInputs = with python.pkgs; [ pip pkgs.jq poetry-core ];
            propagatedBuildInputs = with python.pkgs; [ pythoneda-base ];

            checkInputs = with python.pkgs; [ pytest ];

            pythonImportsCheck = [ pythonpackage ];

            preBuild = ''
              python -m venv .env
              source .env/bin/activate
              pip install ${pythoneda-base}/dist/pythoneda_base-${pythoneda-base.version}-py${pythonMajorVersion}-none-any.whl
              rm -rf .env
            '';

            postInstall = ''
              mkdir $out/dist
              cp dist/${wheelName} $out/dist
              jq ".url = \"$out/dist/${wheelName}\"" $out/lib/python${pythonMajorMinorVersion}/site-packages/${pnameWithUnderscores}-${version}.dist-info/direct_url.json > temp.json && mv temp.json $out/lib/python${pythonMajorMinorVersion}/site-packages/${pnameWithUnderscores}-${version}.dist-info/direct_url.json
            '';

            meta = with pkgs.lib; {
              inherit description homepage license maintainers;
            };
          };
        pythoneda-artifact-shared-changes-0_0_1a2-for =
          { pythoneda-base, python }:
          pythoneda-artifact-shared-changes-for {
            version = "0.0.1a2";
            inherit pythoneda-base python;
          };
      in rec {
        packages = rec {
          pythoneda-artifact-shared-changes-0_0_1a2-python38 =
            pythoneda-artifact-shared-changes-0_0_1a2-for {
              pythoneda-base =
                pythoneda-base.packages.${system}.pythoneda-base-latest-python38;
              python = pkgs.python38;
            };
          pythoneda-artifact-shared-changes-0_0_1a2-python39 =
            pythoneda-artifact-shared-changes-0_0_1a2-for {
              pythoneda-base =
                pythoneda-base.packages.${system}.pythoneda-base-latest-python39;
              python = pkgs.python39;
            };
          pythoneda-artifact-shared-changes-0_0_1a2-python310 =
            pythoneda-artifact-shared-changes-0_0_1a2-for {
              pythoneda-base =
                pythoneda-base.packages.${system}.pythoneda-base-latest-python310;
              python = pkgs.python310;
            };
          pythoneda-artifact-shared-changes-latest-python38 =
            pythoneda-artifact-shared-changes-0_0_1a2-python38;
          pythoneda-artifact-shared-changes-latest-python39 =
            pythoneda-artifact-shared-changes-0_0_1a2-python39;
          pythoneda-artifact-shared-changes-latest-python310 =
            pythoneda-artifact-shared-changes-0_0_1a2-python310;
          pythoneda-artifact-shared-changes-latest =
            pythoneda-artifact-shared-changes-latest-python310;
          default = pythoneda-artifact-shared-changes-latest;
        };
        defaultPackage = packages.default;
        devShells = rec {
          pythoneda-artifact-shared-changes-0_0_1a2-python38 =
            shared.devShell-for {
              package =
                packages.pythoneda-artifact-shared-changes-0_0_1a2-python38;
              pythoneda-base =
                pythoneda-base.packages.${system}.pythoneda-base-latest-python38;
              python = pkgs.python38;
              inherit pkgs nixpkgsRelease;
            };
          pythoneda-artifact-shared-changes-0_0_1a2-python39 =
            shared.devShell-for {
              package =
                packages.pythoneda-artifact-shared-changes-0_0_1a2-python39;
              pythoneda-base =
                pythoneda-base.packages.${system}.pythoneda-base-latest-python39;
              python = pkgs.python39;
              inherit pkgs nixpkgsRelease;
            };
          pythoneda-artifact-shared-changes-0_0_1a2-python310 =
            shared.devShell-for {
              package =
                packages.pythoneda-artifact-shared-changes-0_0_1a2-python310;
              pythoneda-base =
                pythoneda-base.packages.${system}.pythoneda-base-latest-python310;
              python = pkgs.python310;
              inherit pkgs nixpkgsRelease;
            };
          pythoneda-artifact-shared-changes-latest-python38 =
            pythoneda-artifact-shared-changes-0_0_1a2-python38;
          pythoneda-artifact-shared-changes-latest-python39 =
            pythoneda-artifact-shared-changes-0_0_1a2-python39;
          pythoneda-artifact-shared-changes-latest-python310 =
            pythoneda-artifact-shared-changes-0_0_1a2-python310;
          pythoneda-artifact-shared-changes-latest =
            pythoneda-artifact-shared-changes-latest-python310;
          default = pythoneda-artifact-shared-changes-latest;
        };
      });
}
