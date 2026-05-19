# Station 2 — Elecraft K3S (SSB / Digital)

**Role:** SSB phone + digital modes (FT8, RTTY, etc.). The VGA monitor at this
station is for digital-ops display (waterfall, decoders, message windows).

## On this table

- Elecraft K3S transceiver (Pelican case is marked **"K3S"**)
- Station 2 Laptop
- **External VGA monitor** + VGA cable + monitor power cable
- 12 V DC power supply (from blue UPARC Rubbermaid tub)
- Power strip (from tub)
- InRad desk microphone
- Heil headset adapter (alternative — see Mic options)
- Behringer audio splitter + its wall adapter
- DB9 serial-to-USB adapter (K3S ↔ laptop)
- Coax patch cable with UHF barrel connector

## Hardware setup

Wait until the LAN team confirms **"TR4W Server is up"** before bringing up the laptop in the next section.

- [ ] Place the Pelican case marked **"K3S"** at this table.
- [ ] Place the laptop and the **VGA monitor** on the table.
- [ ] Place a 12 V DC power supply on the table.
- [ ] Connect a power strip from the tub to this station's AC outlet.
- [ ] Open the Pelican case; remove the radio, mic, Heil adapter, and cables.
- [ ] Connect the K3S to its 12 V power supply via Anderson PowerPole.
- [ ] Connect the power supply to the station's power strip via its IEC cable.
- [ ] Connect the **DB9 serial-to-USB adapter** from the K3S to the laptop.
- [ ] Connect a coax patch cable with UHF barrel connector to the K3S's **ANT 1** port.
- [ ] Run coax from this position to the patch panel (along the top wall).
- [ ] Connect the **InRad desk microphone** directly to the K3S mic jack.
- [ ] Set the **Heil adapter** on the table next to the rig.
- [ ] Connect the **Behringer audio splitter** to the K3S's headphone output; power it from the station's power strip via its wall adapter.

### VGA monitor

- [ ] Plug the monitor into the station's power strip.
- [ ] Connect the VGA cable from the laptop to the monitor.
- [ ] Power on the monitor.

(Display mode and any digital-ops software configuration is set by the operator, not the setup crew.)

## Mic options

- **Default:** InRad desk mic is plugged into the K3S.
- **For Heil headset:** unplug the InRad, plug the Heil adapter into the K3S mic jack, plug a Heil headset into the adapter.

## Laptop bring-up

- [ ] Power up the laptop.
- [ ] Confirm WiFi is connected to **TRLOG** (and *not* City-Public).
- [ ] Confirm laptop time has synced (NTP from Pi 400).
- [ ] Start TR4W.
- [ ] Confirm TR4W shows this station connected to the server.

## Verify

- [ ] Log a test QSO and confirm it appears in the live stats on the HDMI monitor (or browse `http://192.168.0.100:8080` from this laptop).

## If something's wrong

See `../troubleshooting.md`. LAN team owns server-side issues; for radio or laptop issues at this station, retrace the steps above.
