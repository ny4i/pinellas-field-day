# Field Day Setup Troubleshooting

Quick reference for diagnosing logging and network issues during setup and operation.

## Expected traffic on the TRLOG network

If a station goes dark from the stats page, or duplicate checking starts
behaving oddly, verify the relevant link is alive.

| From       | To           | Transport             | Purpose                       |
|------------|--------------|-----------------------|-------------------------------|
| Laptops    | **TR4W Server** on Pi 400 | **TCP port 1061** on TRLOG (home-grown TR4W protocol) | Multi-op coordination (dup checks, frequency sharing) |
| Laptops    | **n1mm_view** on Pi 400 | UDP on TRLOG          | QSO broadcasts for stats      |
| Laptops    | Pi 400       | NTP on TRLOG          | Time sync                     |
| Any TRLOG client | Pi 400 `:8080` | HTTP on TRLOG    | Local stats viewing (HDMI monitor's browser, any laptop) |
| Pi 400     | UPARC + SPARC web servers | rsync (over SSH) via City-Public | Stats image upload |

The TR4W Server and n1mm_view processes are **independent**. A station can
fail at one without affecting the other — TR4W coordination can be broken
while QSOs still appear in the stats, or vice versa. Test each path
separately when debugging.

---

See also: [network.md](network.md) for topology.
