init -1 python: 
    mas_background_def = MASFilterableBackground(
        "submod_space",
        "Space",
        MASFilterWeatherMap(
            sunrise=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "image_space_sr",
            }),
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "image_space",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "image_space_n",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "image_space_ss",
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

image image_space_sr = "submods/location_space/submod_assets/location/space/space_sr.png"
image image_space = "submods/location_space/submod_assets/location/space/space.png"
image image_space_n = "submods/location_space/submod_assets/location/space/space_n.png"
image image_space_ss = "submods/location_space/submod_assets/location/space/space_ss.png"