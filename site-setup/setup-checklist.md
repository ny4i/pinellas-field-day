# Field Day Setup Checklist

Phase-by-phase checklist for setup day. Work top-to-bottom; earlier phases
must be done (or in progress) before later phases can start.

Each operating station's gear ships in its own Pelican case. Shared
infrastructure (power strips, Behringer splitters, spare cables, etc.)
lives in the **blue UPARC Rubbermaid tub**.

Related documents:

- [network.md](network.md) — logical network and station-to-rig assignment
- [troubleshooting.md](troubleshooting.md) — expected traffic on TRLOG
- [site-layout.drawio](site-layout.drawio) — physical room layout
- **[station-cards/](station-cards/)** — one-page printable setup cards per station (place on each table on setup day)
- `lan-bringup.md` — Pi 400 / WiFi AP / TR4W Server bring-up (forthcoming)
- `antenna-setup.md` — antennas and patch-panel routing (forthcoming)

---

## Phase 1 — Room infrastructure (LAN + power team)

These items have to happen before any station can power up.

### Power runs

- [ ] Run extension cords so each operating table has its own supply (mains).
- [ ] Connect a power strip (from the blue UPARC Rubbermaid tub) at each
      station.

### Network and server (LAN team)

- [ ] Place the **Linksys router** at its designated location and confirm it's
      broadcasting the **TRLOG** SSID (WiFi `10.0.0.0/24`) and providing the
      wired `192.168.0.0/24` LAN.
- [ ] Power up the Raspberry Pi 400 and confirm both interfaces are up:
      wired Ethernet to the Linksys router (`192.168.0.100`), USB WiFi adapter
      on **City-Public**.
- [ ] Confirm the Python **TR4W Server** script is running on the Pi 400.
- [ ] Confirm the NTP server is reachable from a laptop on TRLOG.
- [ ] Place the portable HDMI monitor at the Pi 400.
- [ ] Announce **"TR4W Server is up"** to the station teams before they
      attempt to start TR4W on the laptops.

See [network.md](network.md) for the topology this phase has to result in.
Detailed bring-up procedure for the Pi 400, WiFi AP, and TR4W Server script
lives in a separate document (forthcoming, `lan-bringup.md`).

---

## Phase 2 — Per-station physical placement (all stations)

Repeat for every station — Station 1, Station 2, Station 3, VHF Station:

- [ ] Place the station's Pelican case at the designated table.
- [ ] Place the station's laptop on the table.
- [ ] Place a 12 V DC power supply (from the Rubbermaid tub) at the station.
- [ ] Open the Pelican case and remove the radio, microphone, and cables.

---

## Phase 3 — Rig-specific connections

### Stations 2 and 3 — Elecraft K3S (Station 2) and K3 (Station 3)

**Printable station cards:**
[Station 2 (K3S)](station-cards/station-2-k3s.md) ·
[Station 3 (K3 CW)](station-cards/station-3-k3-cw.md)

The Pelican case marked **"K3S"** goes to **Station 2**. The other K3 case
goes to **Station 3** (CW). Operationally the setup steps are identical:

- [ ] Connect the K3 to its 12 V power supply via Anderson PowerPole.
- [ ] Connect the power supply to the station's power strip via its IEC cable.
- [ ] Connect the **InRad desk microphone** directly to the K3 mic jack.
- [ ] Take the **Heil adapter** out of the Pelican case and set it on the
      table next to the radio. The adapter is *not* in the default mic
      chain — it's an alternative for operators who prefer a Heil headset.
      To switch: unplug the InRad, plug the Heil adapter into the K3 mic
      jack, plug the Heil headset into the adapter.
- [ ] Connect the DB9 serial-to-USB adapter from the K3 to the laptop.
- [ ] Connect the **Behringer audio splitter** to the K3's headphone output.
- [ ] Plug the Behringer into the station's power strip via its adapter.
- [ ] Connect a coax patch cable with UHF barrel connector to the K3's
      **ANT 1** port.
- [ ] Run coax from the radio position to the patch panel.

#### Station 3 (CW) — additional CW gear

After the standard K3 setup above, also:

- [ ] Connect **WinKey Mini** to the **Key** jack on the back of the K3.
- [ ] Connect WinKey Mini to a USB port on the laptop.
- [ ] Connect the **Bencher paddle** to the WinKey Mini. (Paddle supplied
      by NY4I.)
- [ ] Note: Station 3's coax run is across the room (centre-floor run, not
      along the wall) — see [site-layout](site-layout.drawio).

### Station 1 — Elecraft K4 (SSB, CESSB enabled)

**Printable station card:** [Station 1 (K4)](station-cards/station-1-k4.md)

The K4 stays on SSB because its CESSB feature delivers 6–8 dB of effective
talk power; with only one K4 in the room it is more valuable on SSB than
on CW.

Mic wiring is identical to the K3, so the same InRad + optional Heil
adapter arrangement applies here (see Stations 2 / 3 for the swap procedure).

- [ ] Plug the Anderson PowerPole cable between the 12 V power supply and the K4.
- [ ] Connect the power supply to the station's power strip via its IEC cable.
- [ ] Connect a USB cable between the K4 and the laptop. (K4 has native USB —
      no DB9 serial-to-USB adapter needed.)
- [ ] Connect a coax patch cable with UHF barrel connector to the K4's
      **ANT 1** port.
- [ ] Run coax from the radio position to the patch panel (along the wall).
- [ ] Connect the **InRad desk microphone** directly to the K4 mic jack.
- [ ] Take the **Heil adapter** out of the Pelican case and set it on the
      table — alternative for operators who prefer a Heil headset.
- [ ] Connect the **Behringer audio splitter** to the K4's headphone output;
      power it from the station's power strip via its wall adapter.

### VHF Station — Yaesu FT-897 (6 m)

The VHF Station rig and its setup are owned by **Paul KC4YDY**. Paul brings
the rig, cables, and power, and is responsible for getting it on the air.

Coordination points with the rest of the setup team:

- [ ] Paul runs his own coax to the patch panel (or Paul calls out where his
      coax needs to land).
- [ ] The VHF Station uses the FT-897's **hand microphone** — no Heil
      adapter, no InRad mic at this station.
- [ ] If TR4W logging is in scope for the VHF Station, Paul coordinates the
      laptop and CAT/audio interface for his rig.

---

## Phase 4 — Laptop and network bring-up

For each station's laptop, after Phase 1 (TR4W Server up) is announced:

- [ ] Power up the laptop.
- [ ] Confirm WiFi is connected to **TRLOG** and *not* City-Public.
      (See [network.md](network.md) — City-Public must be removed from saved
      networks on each laptop.)
- [ ] Confirm the laptop has synced time from the Pi 400 (NTP).
- [ ] Start TR4W.
- [ ] If TR4W cannot reach the server, confirm with the LAN team that the
      TR4W Server Python script is still running on the Pi 400 before
      troubleshooting further.
- [ ] Confirm TR4W shows the station connected to the server.

---

## Phase 5 — Final verification

- [ ] At each station: log a test QSO and confirm it appears in the stats
      images generated by the Pi 400.
- [ ] Confirm the HDMI monitor on the Pi 400 shows the live stats display.
- [ ] Confirm the stats images are reachable on **both the UPARC and SPARC
      websites** (Pi 400 → rsync via City-Public → both servers).

