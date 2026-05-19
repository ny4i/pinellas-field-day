# Station 1 — Elecraft K4 (SSB)

**Role:** SSB phone, primary HF voice station.
**Why K4 stays on SSB:** the K4's CESSB feature delivers 6–8 dB of effective
talk power. With only one K4 in the room, it is more valuable on SSB than on CW.

## On this table

- Elecraft K4 transceiver
- Station 1 Laptop
- 12 V DC power supply (from blue UPARC Rubbermaid tub)
- Power strip (from tub)
- InRad desk microphone
- Heil headset adapter (alternative — see Mic options)
- Behringer audio splitter + its wall adapter
- USB cable (K4 ↔ laptop)
- Coax patch cable with UHF barrel connector

## Hardware setup

Wait until the LAN team confirms **"TR4W Server is up"** before bringing up the laptop in the next section.

- [ ] Place the Pelican case marked **"K4"** at this table.
- [ ] Place the laptop on the table.
- [ ] Place a 12 V DC power supply on the table.
- [ ] Connect a power strip from the tub to this station's AC outlet.
- [ ] Open the Pelican case; remove the radio, mic, Heil adapter, and cables.
- [ ] Plug the **Anderson PowerPole** cable between the 12 V supply and the K4.
- [ ] Connect the power supply to the station's power strip via its IEC cable.
- [ ] Connect a **USB cable** between the K4 and the laptop. (K4 has native USB — no DB9 adapter needed.)
- [ ] Connect a coax patch cable with UHF barrel connector to the K4's **ANT 1** port.
- [ ] Run coax from this position to the patch panel (along the top wall).
- [ ] Connect the **InRad desk microphone** directly to the K4 mic jack.
- [ ] Set the **Heil adapter** on the table next to the rig.
- [ ] Connect the **Behringer audio splitter** to the K4's headphone output; power it from the station's power strip via its wall adapter.

## Mic options

- **Default:** InRad desk mic is plugged into the K4.
- **For Heil headset:** unplug the InRad, plug the Heil adapter into the K4 mic jack, plug a Heil headset into the adapter.

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
