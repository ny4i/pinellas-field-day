# Station 3 — Elecraft K3 (CW)

**Role:** CW (primary) — also capable of SSB and Digital. This is the dedicated
CW position with the WinKey Mini and Bencher paddle.

## On this table

- Elecraft K3 transceiver (Pelican case marked **"K3"** — not the "K3S" case)
- Station 3 Laptop
- 12 V DC power supply (from blue UPARC Rubbermaid tub)
- Power strip (from tub)
- InRad desk microphone
- Heil headset adapter (alternative — see Mic options)
- Behringer audio splitter + its wall adapter
- DB9 serial-to-USB adapter (K3 ↔ laptop)
- Coax patch cable with UHF barrel connector
- **WinKey Mini** + USB cable (Pelican case)
- **Bencher paddle** (supplied by NY4I)

**Coax run:** Station 3's coax is the **65 ft RG-8X**. It runs from this position
up the east (right) wall behind Talk-In, across the top wall, and into the
patch panel.

## Hardware setup

Wait until the LAN team confirms **"TR4W Server is up"** before bringing up the laptop in the next section.

- [ ] Place the Pelican case marked **"K3"** at this table.
- [ ] Place the laptop on the table.
- [ ] Place a 12 V DC power supply on the table.
- [ ] Connect a power strip from the tub to this station's AC outlet.
- [ ] Open the Pelican case; remove the radio, mic, Heil adapter, and cables.
- [ ] Connect the K3 to its 12 V power supply via Anderson PowerPole.
- [ ] Connect the power supply to the station's power strip via its IEC cable.
- [ ] Connect the **DB9 serial-to-USB adapter** from the K3 to the laptop.
- [ ] Connect the **65 ft RG-8X** coax patch cable (UHF barrel) to the K3's **ANT 1** port.
- [ ] Run coax from this position east to the right wall, up behind Talk-In, across the top wall, and into the patch panel.
- [ ] Connect the **InRad desk microphone** directly to the K3 mic jack.
- [ ] Set the **Heil adapter** on the table next to the rig.
- [ ] Connect the **Behringer audio splitter** to the K3's headphone output; power it from the station's power strip via its wall adapter.

### CW gear

- [ ] Connect the **WinKey Mini** to the **Key** jack on the back of the K3.
- [ ] Connect the WinKey Mini to a USB port on the laptop.
- [ ] Connect the **Bencher paddle** to the WinKey Mini.

## Mic options

- **Default:** InRad desk mic is plugged into the K3 (kept there in case the station is used for SSB).
- **For Heil headset:** unplug the InRad, plug the Heil adapter into the K3 mic jack, plug a Heil headset into the adapter.

## Laptop bring-up

- [ ] Power up the laptop.
- [ ] Confirm WiFi is connected to **TRLOG** (and *not* City-Public).
- [ ] Confirm laptop time has synced (NTP from Pi 400).
- [ ] Start TR4W.
- [ ] Confirm TR4W shows this station connected to the server.
- [ ] Confirm TR4W sees the WinKey on the expected COM port (for keyer integration).

## Verify

- [ ] Send a test CW string via WinKey and confirm it keys the rig.
- [ ] Log a test QSO and confirm it appears in the live stats on the HDMI monitor (or browse `http://192.168.0.100:8080` from this laptop).

## If something's wrong

See `../troubleshooting.md`. LAN team owns server-side issues; for radio, WinKey, or laptop issues at this station, retrace the steps above.
