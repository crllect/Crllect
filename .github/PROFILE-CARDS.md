# Profile cards

The six SVGs in `profile/` are served directly from this repository. The
`Update profile cards` workflow renders them on GitHub's runner every 12 hours
(00:23 and 12:23 UTC), when its configuration changes on `main`, or through
**Actions → Update profile cards → Run workflow**.

The generators retain the Tokyo Night theme and the README's existing layout:

- [Profile summary](https://github.com/vn7n24fzkq/github-profile-summary-cards)
- [Daily and weekly streaks](https://github.com/DenverCoder1/github-readme-streak-stats)
- [Trophies](https://github.com/soulteary/github-profile-trophy-action)
- [Stats and languages](https://github.com/stats-organization/github-readme-stats-action)

Actions are pinned to commit SHAs, and the trophy binary and stats renderer
versions are pinned in the workflow. To upgrade, update those pins together
with any changed inputs.

The workflow uses the built-in `GITHUB_TOKEN` by default. For broader account
statistics or private contributions, optionally add a repository Actions secret
named `PROFILE_TOKEN` containing a personal access token with the appropriate
read access. Private totals depend on that token's permissions and your GitHub
profile's contribution visibility settings. Never put a token in an image URL.

Only the six SVGs are committed, after every generator and SVG validation
succeeds. If GitHub's API or a generator fails, the last saved images remain
available; check the workflow logs and rerun it to refresh. A failure never
publishes a partial set or intentionally replaces a card with an error image.

Validate saved images locally with:

```sh
python3 .github/scripts/validate-profile-cards.py
```

The skill icons and live profile-view counter still use their original services.
WakaTime continues to use its separate README workflow.
