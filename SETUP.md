# Setup

1. Create a public GitHub repository named exactly `AbhishekPandey2005`.
2. Upload the contents of this folder to its `main` branch.
3. Open **Settings > Secrets and variables > Actions > New repository secret**.
4. Create `BIRTH_DATE` with your birth date in `YYYY-MM-DD` format.
5. Open **Actions > Update profile > Run workflow** once.

The built-in `GITHUB_TOKEN` is used automatically. The workflow only requests
permission to write the generated SVG files back to this repository.

To add your portfolio later, replace `coming soon` in `profile.py` and add its
link to the centered link row in `README.md`.
