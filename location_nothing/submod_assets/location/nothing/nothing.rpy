init -1 python: 
    mas_background_def = MASFilterableBackground(
        "submod_nothing",
        "Nothing",
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "image_nothing",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "image_nothing",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "image_nothing",
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
        disable_progressive=False,
        hide_masks=False,
        unlocked=True,
        entry_pp=store.mas_background._def_background_entry,
        exit_pp=store.mas_background._def_background_exit,
    )

    #Now load data
    store.mas_background.loadMBGData()

image image_nothing = "submods/location_nothing/submod_assets/location/nothing/nothing.png"