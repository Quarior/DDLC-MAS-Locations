init -1 python: 
    mas_background_def = MASFilterableBackground(
        "submod_void",
        "Void",
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "image_void",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "image_void",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "image_void",
            }),
        ),
        MASBackgroundFilterManager(
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            ),
            MASBackgroundFilterChunk(
                True,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_DAY,
                    60
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
            ),
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            )
        ),
        hide_calendar=True,
        disable_progressive=True,
        hide_masks=True,
        unlocked=True,
        entry_pp=store.mas_background._def_background_entry,
        exit_pp=store.mas_background._def_background_exit,
    )

    #Now load data
    store.mas_background.loadMBGData()

image image_void = "submods/location_void/submod_assets/location/void/void.png"