# Uptime Kuma API Fork

This is a fork of [lucasheld/uptime-kuma-api](https://github.com/lucasheld/uptime-kuma-api) with additional support for Uptime Kuma 2.0.

## Why This Fork?

The upstream library currently supports Uptime Kuma versions 1.21.3 - 1.23.2. This fork merges open PRs that add support for Uptime Kuma 2.0.x.

## Merged PRs

The following PRs from upstream have been merged into this fork:

### V2.0 Support
- **PR #86**: feat: Uptime monitors to support 2.0 (by @markus-seidl)
- **PR #87**: Fix `save_status_page` for v2.0.2 by removing `autoRefreshInterval` (by @relic-se)
- **PR #88**: Add conditions option to DNS monitors (by @relic-se)

### Bug Fixes & Improvements
- **PR #57**: fix type for notificationIDList in _build_monitor_data() (by @obfusk)
- **PR #60**: Update api.py - call out API key usage specifically (by @nneul)
- **PR #67**: Missing import (by @glerb)
- **PR #69**: Fixed datatype for smtpSecure property to bool (by @BergCyrill)
- **PR #80**: Fixed error in README.md (by @VadymKhvoinytskyi)
- **PR #81**: Add Ssl property to request allow SelfSignedSSl uptime (by @pr0kium)
- **PR #84**: add support for passing json path operator while adding monitor (by @karuppiah7890)
- **PR #90**: fix docstring about pagerduty where mandatory was inverse (by @LeBaronDeCharlus)

### Additional Fixes
- Fixed duplicate parameter conflicts from merged PRs (`jsonPathOperator`, `conditions`)
- Added `requests` to dependencies (required by v2.0 support)

## Installation

```bash
# From this fork's v2-support branch
pip install git+https://github.com/mmeyer/uptime-kuma-api.git@v2-support

# Or with pinned commit (recommended for production)
pip install git+https://github.com/mmeyer/uptime-kuma-api.git@ad9db41
```

### For pyproject.toml (uv/poetry)
```toml
dependencies = [
    "uptime-kuma-api @ git+https://github.com/mmeyer/uptime-kuma-api.git@v2-support",
]
```

### For requirements.txt
```
uptime-kuma-api @ git+https://github.com/mmeyer/uptime-kuma-api.git@v2-support
```

## Tested Compatibility

- Uptime Kuma 2.0.2 (tested)
- Uptime Kuma 1.23.x (should work, inherited from upstream)

## Usage

```python
from uptime_kuma_api import UptimeKumaApi, MonitorType

# Connect to Uptime Kuma
api = UptimeKumaApi("http://your-uptime-kuma:3001")

# Login (use api.login() without args when disableAuth=True)
api.login()  # or api.login("username", "password")

# Get server info
info = api.info()
print(f"Version: {info.get('version')}")

# List monitors
monitors = api.get_monitors()

# Create HTTP monitor
api.add_monitor(
    type=MonitorType.HTTP,
    name="My Service",
    url="https://example.com",
    interval=60
)

# Create TCP port monitor
api.add_monitor(
    type=MonitorType.PORT,
    name="My Database",
    hostname="10.0.0.1",
    port=5432,
    interval=60
)

# Disconnect when done
api.disconnect()
```

## Keeping Up to Date

To sync with upstream and re-merge PRs:

```bash
cd uptime-kuma-api
git fetch upstream
git checkout master
git merge upstream/master
git checkout v2-support
git rebase master
# Re-apply any custom changes if needed
git push -f origin v2-support
```

## Migration Back to Upstream

When upstream officially supports v2.0, migration should be straightforward:

1. Update your requirements to use `uptime-kuma-api` from PyPI
2. Remove the git URL reference
3. Test thoroughly

## Known Differences from Upstream

- **monitorID vs monitorId**: v2.0 returns `monitorID` (capital ID) instead of `monitorId` in `add_monitor` response. Handle both:
  ```python
  result = api.add_monitor(...)
  monitor_id = result.get('monitorID') or result.get('monitorId')
  ```

## Maintainer

Fork maintained by: @mmeyer
Last updated: 2024-12
