# Field Day Logging & Stats Network

Logical topology of the on-site logging and stats network for ARRL Field Day.

## Topology

```mermaid
flowchart LR
    subgraph TRLOG["TRLOG WiFi  -  192.168.0.0/24"]
        direction TB
        AP["WiFi AP / Switch<br/><b>SSID: TRLOG</b>"]
        PI["Raspberry Pi 400<br/>192.168.0.100<br/>──────────<br/>TR4W Server (Python)<br/>NTP server<br/>n1mm_view (stats)<br/>Web UI on :8080<br/>rsync publisher"]
        L1["Station 1<br/><i>K4 — SSB</i>"]
        L2["Station 2<br/><i>K3S — SSB / Digital</i>"]
        L3["Station 3<br/><i>K3 — CW</i>"]
        LV["VHF Station<br/><i>FT-897 — 6m</i>"]
        L1 -. WiFi .- AP
        L2 -. WiFi .- AP
        L3 -. WiFi .- AP
        LV -. WiFi .- AP
        AP -. WiFi .- PI
    end
    MON["Portable<br/>HDMI Monitor"]
    NET(("City-Public<br/>WiFi"))
    WEB1[/"UPARC web server"/]
    WEB2[/"SPARC web server"/]
    PI --- MON
    PI -. 2nd WiFi .- NET
    NET ==>|rsync| WEB1
    NET ==>|rsync| WEB2

    classDef pi fill:#ffe8b3,stroke:#a06b00,stroke-width:2px,color:#000
    classDef ap fill:#cfe6ff,stroke:#0050a0,stroke-width:2px,color:#000
    classDef laptop fill:#ffffff,stroke:#333,color:#000
    classDef ext fill:#eeeeee,stroke:#666,stroke-dasharray:4 2,color:#000
    class PI pi
    class AP ap
    class L1,L2,L3,LV laptop
    class NET,WEB1,WEB2,MON ext
```

**Legend:** dotted = WiFi · solid = HDMI · double arrow = rsync publish

---

## What runs on the Pi 400

The Pi 400 is now the *only* server. The previous Windows TR4W Server box
(`192.168.0.12`, wired Ethernet) is **gone**. Its functions have been
re-implemented as a Python script that runs on the Pi alongside the existing
stats workload.

**The TR4W Server and the n1mm_view stats stack are independent processes**
running on the same Pi. They share the host but not state — TR4W
coordination can fail while QSOs still reach the stats, or vice versa.
See [troubleshooting.md](troubleshooting.md) for the traffic flows.

| Service                | Purpose                                                    |
|------------------------|------------------------------------------------------------|
| TR4W Server (Python)   | Coordinates the four TR4W laptops (multi-op dup checks etc.) |
| NTP server             | Time sync source for all four laptops                      |
| **n1mm_view** (`~/n1mm_view`) | Receives UDP QSO broadcasts from the laptops; renders stats images (band / score / rate graphics) to a **RAM disk** on the Pi |
| **Local web server** `:8080`  | Serves the stats images on TRLOG — the HDMI monitor browses to it, and any laptop on TRLOG can view it too at `http://192.168.0.100:8080` |
| **rsync publisher**    | Whenever the RAM-disk images update, rsyncs them to the **UPARC** and **SPARC** web servers |

## Two WiFi interfaces — important

The Pi 400 is **dual-homed** by design. The two networks must not be confused:

| Interface          | SSID         | Purpose                                              |
|--------------------|--------------|------------------------------------------------------|
| Built-in WiFi      | **TRLOG**    | Talks to the logging laptops; static `192.168.0.100` |
| USB WiFi adapter   | **City-Public** | Internet uplink — for publishing stats *only*     |

## Laptop setup — non-negotiable

Each station's laptop **must** be configured to:

1. Connect **only to TRLOG** (set "connect automatically" on TRLOG).
2. Have **City-Public removed from saved networks** — especially personal laptops
   that may have joined it in past years.
3. Use the Pi 400 as its NTP source.

If a laptop silently auto-joins City-Public it leaves the TRLOG network,
TR4W coordination breaks for that station, and its QSOs stop reaching the
stats listener. This has bitten us in past years — verify on setup day.

## Changes from previous year

- **Removed:** Windows TR4W Server box (`192.168.0.12`, wired Ethernet to switch).
- **Added:** Python TR4W Server script on the Pi 400 — the Pi now performs
  *both* coordination and stats roles.
- **Station naming:** stations are now "Station 1 / 2 / 3 / VHF Station"
  (previously "TR4W Laptop VHF / 1 / 2 / 3").
- **Station 1 rig:** Elecraft K4 replaces the K3. Stays on SSB — the K4's CESSB
  feature gives 6–8 dB of effective talk power, so with only one K4 in the
  room it is more valuable on SSB than on CW.
- **VHF Station rig:** Yaesu FT-897 replaces the IC-7600 6m station.

---

See also: [troubleshooting.md](troubleshooting.md) for expected traffic and failure modes.
