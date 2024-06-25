# board: [ platform, uf2_family, manual core URL]
ALL_PLATFORMS={
    # classic Arduino AVR
    "uno" : ["arduino:avr:uno", None, None],
    "leonardo" : ["arduino:avr:leonardo", None, None],
    "mega2560" : ["arduino:avr:mega:cpu=atmega2560", None, None],
    # Arduino SAMD
    "zero" : ["arduino:samd:arduino_zero_native", "0x68ed2b88", None, None],
    "cpx" : ["arduino:samd:adafruit_circuitplayground_m0", "0x68ed2b88", None],
    # Espressif
    "esp8266" : ["esp8266:esp8266:huzzah:eesz=4M3M,xtal=80", None, None],
    "esp32" : ["esp32:esp32:featheresp32:FlashFreq=80", None, None],
    "itsybitsy_esp32" : ["esp32:esp32:adafruit_itsybitsy_esp32:FlashFreq=80", None, None],
    "feather_esp8266" : ["esp8266:esp8266:huzzah:xtal=80,vt=flash,exception=disabled,stacksmash=disabled,ssl=all,mmu=3232,non32xfer=fast,eesz=4M2M,ip=lm2f,dbg=Disabled,lvl=None____,wipe=none,baud=115200", None, None],
    "feather_esp32" : ["esp32:esp32:featheresp32:FlashFreq=80", None, None],
    "wippersnapper_feather_esp32" : ["esp32:esp32:featheresp32:FlashFreq=80,PartitionScheme=min_spiffs", None, None],
    "feather_esp32_v2" : ["esp32:esp32:adafruit_feather_esp32_v2", None, None],
    "qtpy_esp32" : ["esp32:esp32:adafruit_qtpy_esp32_pico", None, None],
    "qtpy_esp32c3" : ["esp32:esp32:adafruit_qtpy_esp32c3:FlashMode=qio", None, None],
    "wippersnapper_qtpy_esp32c3" : ["esp32:esp32:adafruit_qtpy_esp32c3:FlashMode=qio,PartitionScheme=min_spiffs", None, None],
    ## ESP32-S2
    "magtag" : ["esp32:esp32:adafruit_magtag29_esp32s2", "0xbfdd4eee", None],
    "funhouse" : ["esp32:esp32:adafruit_funhouse_esp32s2", "0xbfdd4eee", None],
    "funhouse_noota" : ["esp32:esp32:adafruit_funhouse_esp32s2:PartitionScheme=tinyuf2_noota", "0xbfdd4eee", None],
    "metroesp32s2" : ["esp32:esp32:adafruit_metro_esp32s2", "0xbfdd4eee", None],
    "qtpy_esp32s2" : ["esp32:esp32:adafruit_qtpy_esp32s2", "0xbfdd4eee", None],
    "feather_esp32s2" : ["esp32:esp32:adafruit_feather_esp32s2", "0xbfdd4eee", None],
    "feather_esp32s2_debug" : ["esp32:esp32:adafruit_feather_esp32s2:DebugLevel=verbose", "0xbfdd4eee", None],
    "feather_esp32s2_tft" : ["esp32:esp32:adafruit_feather_esp32s2_tft", "0xbfdd4eee", None],
    "feather_esp32s2_tft_debug" : ["esp32:esp32:adafruit_feather_esp32s2_tft:DebugLevel=verbose", "0xbfdd4eee", None],
    "feather_esp32s2_reverse_tft" : ["esp32:esp32:adafruit_feather_esp32s2_reversetft", "0xbfdd4eee", None],
    ## ESP32-S3
    "feather_esp32s3" : ["esp32:esp32:adafruit_feather_esp32s3_nopsram", "0xc47e5767", None],
    "feather_esp32s3_debug" : ["esp32:esp32:adafruit_feather_esp32s3_nopsram:DebugLevel=verbose", "0xc47e5767", None],
    "feather_esp32s3_4mbflash_2mbpsram" : ["esp32:esp32:adafruit_feather_esp32s3", "0xc47e5767", None],
    "feather_esp32s3_4mbflash_2mbpsram_debug" : ["esp32:esp32:adafruit_feather_esp32s3:DebugLevel=verbose", "0xc47e5767", None],
    "feather_esp32s3_tft" : ["esp32:esp32:adafruit_feather_esp32s3_tft", "0xc47e5767", None],
    "feather_esp32s3_tft_debug" : ["esp32:esp32:adafruit_feather_esp32s3_tft:DebugLevel=verbose", "0xc47e5767", None],
    "feather_esp32s3_reverse_tft" : ["esp32:esp32:adafruit_feather_esp32s3_reversetft", "0xc47e5767", None],
    "feather_esp32s3_reverse_tft_debug" : ["esp32:esp32:adafruit_feather_esp32s3_reversetft:DebugLevel=verbose", "0xc47e5767", None],
    "matrixportal_s3" : ["esp32:esp32:adafruit_matrixportal_esp32s3", "0xc47e5767", None],
    "metro_esp32s3" : ["esp32:esp32:adafruit_metro_esp32s3", "0xc47e5767", None],
    "pycamera_s3" : ["esp32:esp32:adafruit_camera_esp32s3", "0xc47e5767", None],
    "qualia_s3_rgb666" : ["esp32:esp32:adafruit_qualia_s3_rgb666", "0xc47e5767", None],
    "qtpy_esp32s3" : ["esp32:esp32:adafruit_qtpy_esp32s3_nopsram", "0xc47e5767", None],
    "qtpy_esp32s3_n4r2" : ["esp32:esp32:adafruit_qtpy_esp32s3_n4r2", "0xc47e5767", None],
    # Adafruit AVR
    "trinket_3v" : ["adafruit:avr:trinket3", None, None],
    "trinket_5v" : ["adafruit:avr:trinket5", None, None],
    "protrinket_3v" : ["adafruit:avr:protrinket3", None, None],
    "protrinket_5v" : ["adafruit:avr:protrinket5", None, None],
    "gemma" : ["adafruit:avr:gemma", None, None],
    "flora" : ["adafruit:avr:flora8", None, None],
    "feather32u4" : ["adafruit:avr:feather32u4", None, None],
    "cpc" : ["arduino:avr:circuitplay32u4cat", None, None],
    # Adafruit SAMD
    "gemma_m0" : ["adafruit:samd:adafruit_gemma_m0", "0x68ed2b88", None],
    "trinket_m0" : ["adafruit:samd:adafruit_trinket_m0", "0x68ed2b88", None],
    "feather_m0_express" : ["adafruit:samd:adafruit_feather_m0_express", "0x68ed2b88", None],
    "feather_m0_express_tinyusb" : ["adafruit:samd:adafruit_feather_m0_express:usbstack=tinyusb", "0x68ed2b88", None],
    "feather_m4_express" : ["adafruit:samd:adafruit_feather_m4:speed=120", "0x55114460", None],
    "feather_m4_express_tinyusb" : ["adafruit:samd:adafruit_feather_m4:speed=120,usbstack=tinyusb", "0x55114460", None],
    "feather_m4_can" : ["adafruit:samd:adafruit_feather_m4_can:speed=120", "0x55114460", None],
    "feather_m4_can_tinyusb" : ["adafruit:samd:adafruit_feather_m4_can:speed=120,usbstack=tinyusb", "0x55114460", None],
    "metro_m0" : ["adafruit:samd:adafruit_metro_m0", "0x68ed2b88", None],
    "metro_m0_tinyusb" : ["adafruit:samd:adafruit_metro_m0:usbstack=tinyusb", "0x68ed2b88", None],
    "metro_m4" : ["adafruit:samd:adafruit_metro_m4:speed=120", "0x55114460", None],
    "metro_m4_tinyusb" : ["adafruit:samd:adafruit_metro_m4:speed=120,usbstack=tinyusb", "0x55114460", None],
    "metro_m4_airliftlite" : ["adafruit:samd:adafruit_metro_m4_airliftlite:speed=120", "0x55114460", None],
    "metro_m4_airliftlite_tinyusb" : ["adafruit:samd:adafruit_metro_m4_airliftlite:speed=120,usbstack=tinyusb", "0x55114460", None],
    "pybadge" : ["adafruit:samd:adafruit_pybadge_m4:speed=120", "0x55114460", None],
    "pybadge_tinyusb" : ["adafruit:samd:adafruit_pybadge_m4:speed=120,usbstack=tinyusb", "0x55114460", None],
    "pygamer" : ["adafruit:samd:adafruit_pygamer_m4:speed=120", "0x55114460", None],
    "pygamer_tinyusb" : ["adafruit:samd:adafruit_pygamer_m4:speed=120,usbstack=tinyusb", "0x55114460", None],
    "hallowing_m0" : ["adafruit:samd:adafruit_hallowing", "0x68ed2b88", None],
    "hallowing_m4" : ["adafruit:samd:adafruit_hallowing_m4:speed=120", "0x55114460", None],
    "hallowing_m4_tinyusb" : ["adafruit:samd:adafruit_hallowing_m4:speed=120,usbstack=tinyusb", "0x55114460", None],
    "neotrellis_m4" : ["adafruit:samd:adafruit_trellis_m4:speed=120", "0x55114460", None],
    "monster_m4sk" : ["adafruit:samd:adafruit_monster_m4sk:speed=120", "0x55114460", None],
    "monster_m4sk_tinyusb" : ["adafruit:samd:adafruit_monster_m4sk:speed=120,usbstack=tinyusb", "0x55114460", None],
    "pyportal" : ["adafruit:samd:adafruit_pyportal_m4:speed=120", "0x55114460", None],
    "pyportal_tinyusb" : ["adafruit:samd:adafruit_pyportal_m4:speed=120,usbstack=tinyusb", "0x55114460", None],
    "pyportal_titano" : ["adafruit:samd:adafruit_pyportal_m4_titano:speed=120", "0x55114460", None],
    "pyportal_titano_tinyusb" : ["adafruit:samd:adafruit_pyportal_m4_titano:speed=120,usbstack=tinyusb", "0x55114460", None],
    "cpx_ada" : ["adafruit:samd:adafruit_circuitplayground_m0", "0x68ed2b88", None],
    "grand_central" : ["adafruit:samd:adafruit_grandcentral_m4:speed=120", "0x55114460", None],
    "grand_central_tinyusb" : ["adafruit:samd:adafruit_grandcentral_m4:speed=120,usbstack=tinyusb", "0x55114460", None],
    "matrixportal" : ["adafruit:samd:adafruit_matrixportal_m4:speed=120", "0x55114460", None],
    "matrixportal_tinyusb" : ["adafruit:samd:adafruit_matrixportal_m4:speed=120,usbstack=tinyusb", "0x55114460", None],
    "neotrinkey_m0" : ["adafruit:samd:adafruit_neotrinkey_m0", "0x68ed2b88", None],
    "rotarytrinkey_m0" : ["adafruit:samd:adafruit_rotarytrinkey_m0", "0x68ed2b88", None],
    "neokeytrinkey_m0" : ["adafruit:samd:adafruit_neokeytrinkey_m0", "0x68ed2b88", None],
    "slidetrinkey_m0" : ["adafruit:samd:adafruit_slidetrinkey_m0", "0x68ed2b88", None],
    "proxlighttrinkey_m0" : ["adafruit:samd:adafruit_proxlighttrinkey_m0", "0x68ed2b88", None],
    "trrstrinkey_m0" : ["adafruit:samd:adafruit_trrstrinkey_m0", "0x68ed2b88", None],
    "thumbsticktrinkey_m0" : ["adafruit:samd:adafruit_thumbsticktrinkey_m0", "0x68ed2b88", None],
    "sht4xtrinkey_m0" : ["adafruit:samd:adafruit_sht4xtrinkey_m0", "0x68ed2b88", None],
    "pixeltrinkey_m0" : ["adafruit:samd:adafruit_pixeltrinkey_m0", "0x68ed2b88", None],
    "X_m0" : ["adafruit:samd:adafruit_X_m0", "0x68ed2b88", None],
    "qtpy_m0" : ["adafruit:samd:adafruit_qtpy_m0", "0x68ed2b88", None],
    "qtpy_m0_tinyusb" : ["adafruit:samd:adafruit_qtpy_m0:usbstack=tinyusb", "0x68ed2b88", None],
    # Arduino SAMD
    "mkrwifi1010" : ["arduino:samd:mkrwifi1010", "0x8054", None],
    "nano_33_iot" : ["arduino:samd:nano_33_iot", "0x8057", None],
    # Arduino nRF
    "microbit" : ["sandeepmistry:nRF5:BBCmicrobit:softdevice=s110", None, None],
    # Adafruit nRF
    "nrf52832" : ["adafruit:nrf52:feather52832:softdevice=s132v6,debug=l0", None, None],
    "nrf52840" : ["adafruit:nrf52:feather52840:softdevice=s140v6,debug=l0", "0xada52840", None],
    "cpb" : ["adafruit:nrf52:cplaynrf52840:softdevice=s140v6,debug=l0", "0xada52840", None],
    "clue" : ["adafruit:nrf52:cluenrf52840:softdevice=s140v6,debug=l0", "0xada52840", None],
    "ledglasses_nrf52840" : ["adafruit:nrf52:ledglasses_nrf52840:softdevice=s140v6,debug=l0", "0xada52840", None],
    # RP2040 (Philhower)
    "pico_rp2040" : ["rp2040:rp2040:rpipico:freq=125,flash=2097152_0", "0xe48bff56", None],
    "pico_rp2040_tinyusb" : ["rp2040:rp2040:rpipico:flash=2097152_0,freq=120,dbgport=Disabled,dbglvl=None,usbstack=tinyusb", "0xe48bff56", None],
    "pico_rp2040_tinyusb_host" : ["rp2040:rp2040:rpipico:flash=2097152_0,freq=120,dbgport=Disabled,dbglvl=None,usbstack=tinyusb_host", "0xe48bff56", None],
    "picow_rp2040" : ["rp2040:rp2040:rpipicow:flash=2097152_0,freq=125", "0xe48bff56", None],
    "picow_rp2040_tinyusb" : ["rp2040:rp2040:rpipicow:flash=2097152_131072,freq=120,dbgport=Disabled,dbglvl=None,usbstack=tinyusb", "0xe48bff56", None],
    "feather_rp2040" : ["rp2040:rp2040:adafruit_feather:freq=125,flash=8388608_0", "0xe48bff56", None],
    "feather_rp2040_tinyusb" : ["rp2040:rp2040:adafruit_feather:flash=8388608_0,freq=120,dbgport=Disabled,dbglvl=None,usbstack=tinyusb", "0xe48bff56", None],
    "feather_rp2040_rfm" : ["rp2040:rp2040:adafruit_feather_rfm:freq=125,flash=8388608_0", "0xe48bff56", None],
    "feather_rp2040_rfm_tinyusb" : ["rp2040:rp2040:adafruit_feather_rfm:flash=8388608_0,freq=120,dbgport=Disabled,dbglvl=None,usbstack=tinyusb", "0xe48bff56", None],
    "feather_rp2040_dvi" : ["rp2040:rp2040:adafruit_feather_dvi:freq=125,flash=8388608_0", "0xe48bff56", None],
    "feather_rp2040_dvi_tinyusb" : ["rp2040:rp2040:adafruit_feather_dvi:flash=8388608_0,freq=120,dbgport=Disabled,dbglvl=None,usbstack=tinyusb", "0xe48bff56", None],
    "feather_rp2040_usbhost_tinyusb" : ["rp2040:rp2040:adafruit_feather_usb_host:flash=8388608_0,freq=120,dbgport=Disabled,dbglvl=None,usbstack=tinyusb", "0xe48bff56", None],
    "qt2040_trinkey" : ["rp2040:rp2040:adafruit_trinkeyrp2040qt:freq=125,flash=8388608_0", "0xe48bff56", None],
    "qt2040_trinkey_tinyusb" : ["rp2040:rp2040:adafruit_trinkeyrp2040qt:flash=8388608_0,freq=120,dbgport=Disabled,dbglvl=None,usbstack=tinyusb", "0xe48bff56", None],
    "qt_py_rp2040": ["rp2040:rp2040:adafruit_qtpy:freq=125,flash=8388608_0", "0xe48bff56", None],
    "qt_py_rp2040_tinyusb": ["rp2040:rp2040:adafruit_qtpy:flash=8388608_0,freq=120,dbgport=Disabled,dbglvl=None,usbstack=tinyusb", "0xe48bff56", None],
    "itsybitsy_rp2040" : ["rp2040:rp2040:adafruit_itsybitsy:freq=125,flash=8388608_524288", "0xe48bff56", None],
    "itsybitsy_rp2040_tinyusb" : ["rp2040:rp2040:adafruit_itsybitsy:flash=8388608_524288,freq=120,dbgport=Disabled,dbglvl=None,usbstack=tinyusb", "0xe48bff56", None],

    # Attiny8xy, 16xy, 32xy (SpenceKonde)
    "attiny3217" : ["megaTinyCore:megaavr:atxy7:chip=3217", None, None],
    "attiny3216" : ["megaTinyCore:megaavr:atxy6:chip=3216", None, None],
    "attiny1617" : ["megaTinyCore:megaavr:atxy7:chip=1617", None, None],
    "attiny1616" : ["megaTinyCore:megaavr:atxy6:chip=1616", None, None],
    "attiny1607" : ["megaTinyCore:megaavr:atxy7:chip=1607", None, None],
    "attiny1606" : ["megaTinyCore:megaavr:atxy6:chip=1606", None, None],
    "attiny817" : ["megaTinyCore:megaavr:atxy7:chip=817", None, None],
    "attiny816" : ["megaTinyCore:megaavr:atxy6:chip=816", None, None],
    "attiny807" : ["megaTinyCore:megaavr:atxy7:chip=807", None, None],
    "attiny806" : ["megaTinyCore:megaavr:atxy6:chip=806", None, None],

    # CH32v2 (openwch)
    "CH32V20x_EVT": ["WCH:ch32v:CH32V20x_EVT", None, None],

    # groupings
    "main_platforms" : ("uno", "leonardo", "mega2560", "zero", "qtpy_m0",
                        "esp8266", "esp32", "metro_m4", "trinket_m0"),
    "arcada_platforms" : ("pybadge", "pygamer", "hallowing_m4",
                          "cpb", "cpx_ada"),
    "wippersnapper_platforms" : ("metro_m4_airliftlite_tinyusb", "pyportal_tinyusb"),
    "rp2040_platforms" : ("pico_rp2040", "feather_rp2040")
}
