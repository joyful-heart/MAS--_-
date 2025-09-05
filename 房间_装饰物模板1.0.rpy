#======================================================================
# MAS 背景装饰物模板
# 描述: 为 Monika After Story 模组提供背景的节日装饰功能
# 包含万圣节(o31)和圣诞节(d25)装饰物
#======================================================================

# 标签说明:
# - 标签中含有 o31 表示万圣节相关装饰
# - 标签中含有 d25 表示圣诞节相关装饰
# 
# 使用说明:
# 1. 创建好对应的文件夹结构
# 2. 修改以下配置和图像路径
# 3. 只有装饰物部分用于制作节日装饰
#======================================================================


#======================================================================
#使用教程：例
#======================================================================
# 标签用xxx_o31_ceiling_lights能便于区分
image dormitory_o31_ceiling_lights = MASFilterableSprite(
    "mod_assets/location/dormitory/deco/o31/ceiling_lights.png",#图片路径
    highlight=MASFilterMap(night="0")  # 夜晚夜晚显示灯光
)#灯光路径"mod_assets/location/dormitory/deco/o31/ceiling_lights-h0.png"
init 501 python:
    # 注册万圣节天花板灯光
    MASImageTagDecoDefinition.register_img(
        "mas_o31_ceiling_lights",#原图片标签不可动
        submod_background_dormitory.background_id,#背景id
        MASAdvancedDecoFrame(zorder=5),  # 设置图层顺序
        replace_tag="dormitory_o31_ceiling_lights"#需要注册的标签
    )




##############################主体部分##################################

#======================================================================
# 万圣节(o31)装饰物定义
#======================================================================

# 万圣节天花板灯光装饰
image dormitory_o31_ceiling_lights = MASFilterableSprite(
    "mod_assets/location/dormitory/deco/o31/ceiling_lights.png",
    highlight=MASFilterMap(night="0")  # 夜晚显示灯光
)

# 万圣节蜡烛装饰
image dormitory_o31_candles = MASFilterableSprite(
    "mod_assets/location/dormitory/deco/o31/candles.png",
    highlight=MASFilterMap(night="0")  # 夜晚显示灯光
)

# 万圣节南瓜灯装饰
image dormitory_o31_jack_o_lantern = MASFilterableSprite(
    "mod_assets/location/dormitory/deco/o31/jackolantern.png",
    highlight=MASFilterMap(night="0")  # 夜晚显示灯光
)

# 万圣节墙上的蜡烛装饰
image dormitory_o31_wall_candle = MASFilterableSprite(
    "mod_assets/location/dormitory/deco/o31/wall_candle.png",
    highlight=MASFilterMap(night="0")  # 夜晚显示灯光
)

# 万圣节猫框架动画 - 多个猫图像随机切换
image dormitory_o31_cat_frame:
    block:
        choice:  # 随机选择猫的不同姿势
            MASFilterSwitch("mod_assets/location/dormitory/deco/o31/ATL/cat_0.png")
        choice:
            MASFilterSwitch("mod_assets/location/dormitory/deco/o31/ATL/cat_01.png")
        choice:
            MASFilterSwitch("mod_assets/location/dormitory/deco/o31/ATL/cat_01-1.png")
        choice:
            MASFilterSwitch("mod_assets/location/dormitory/deco/o31/ATL/cat_01-2.png")
        choice:
            MASFilterSwitch("mod_assets/location/dormitory/deco/o31/ATL/cat_01-3.png")
        choice:
            MASFilterSwitch("mod_assets/location/dormitory/deco/o31/ATL/cat_02.png")
        choice:
            MASFilterSwitch("mod_assets/location/dormitory/deco/o31/ATL/cat_02-1.png")
        choice:
            MASFilterSwitch("mod_assets/location/dormitory/deco/o31/ATL/cat_02-2.png")
        choice:
            MASFilterSwitch("mod_assets/location/dormitory/deco/o31/ATL/cat_02-3.png")
    30  # 每帧显示30秒
    repeat  # 循环播放

# 万圣节挂幅
image dormitory_o31_garlands = MASFilterSwitch("mod_assets/location/dormitory/deco/o31/garland.png")

# 万圣节蜘蛛网装饰
image dormitory_o31_cobwebs = MASFilterSwitch("mod_assets/location/dormitory/deco/o31/wall_webs.png")

# 万圣节窗户幽灵装饰
image dormitory_o31_window_ghost = MASFilterSwitch("mod_assets/location/dormitory/deco/o31/window_ghost.png")

# 万圣节天花板装饰
image dormitory_o31_ceiling_deco = MASFilterSwitch("mod_assets/location/dormitory/deco/o31/ceiling_deco.png")

# 万圣节墙上蝙蝠装饰
image dormitory_o31_wall_bats = MASFilterSwitch("mod_assets/location/dormitory/deco/o31/wall_bats.png")

# 万圣节渐晕效果 - 用于营造氛围
image dormitory_o31_vignette = Image("mod_assets/location/dormitory/deco/o31/vignette.png")

#======================================================================
# 圣诞节(d25)装饰物定义
#======================================================================

# 圣诞节横幅装饰
image dormitory_d25_banners = MASFilterSwitch(
    "mod_assets/location/dormitory/deco/d25/bgdeco.png"
)

# 圣诞节榭寄生装饰
image mas_mistletoe = MASFilterSwitch(
    "mod_assets/location/dormitory/deco/d25/mistletoe.png"
)

# 圣诞节灯光装饰 - 根据时间和动画设置切换不同状态
image dormitory_d25_lights = ConditionSwitch(
    "mas_isNightNow()", ConditionSwitch(  # 如果是夜晚
        "persistent._mas_disable_animations", "mod_assets/location/dormitory/deco/d25/lights_on_1.png",  # 如果禁用动画，使用静态灯光
        "not persistent._mas_disable_animations", "dormitory_d25_night_lights_atl"  # 否则使用动画灯光
    ),
    "True", MASFilterSwitch("mod_assets/location/dormitory/deco/d25/lights_off.png")  # 白天时灯光关闭
)

# 圣诞节夜晚灯光动画
image dormitory_d25_night_lights_atl:
    block:
        "mod_assets/location/dormitory/deco/d25/lights_on_1.png"  # 第一帧灯光
        0.5  # 显示0.5秒
        "mod_assets/location/dormitory/deco/d25/lights_on_2.png"  # 第二帧灯光
        0.5  # 显示0.5秒
        "mod_assets/location/dormitory/deco/d25/lights_on_3.png"  # 第三帧灯光
        0.5  # 显示0.5秒
    repeat  # 循环播放

# 圣诞节花环装饰 - 根据时间和动画设置切换不同状态
image dormitory_d25_garlands = ConditionSwitch(
    "mas_isNightNow()", ConditionSwitch(  # 如果是夜晚
        "persistent._mas_disable_animations", "mod_assets/location/dormitory/deco/d25/garland_on_1.png",  # 如果禁用动画，使用静态花环
        "not persistent._mas_disable_animations", "dormitory_d25_night_garlands_atl"  # 否则使用动画花环
    ),
    "True", MASFilterSwitch("mod_assets/location/dormitory/deco/d25/garland.png")  # 白天时花环无灯光
)

# 圣诞节夜晚花环动画
image dormitory_d25_night_garlands_atl:
    "mod_assets/location/dormitory/deco/d25/garland_on_1.png"  # 初始帧
    block:
        "mod_assets/location/dormitory/deco/d25/garland_on_1.png" with Dissolve(3, alpha=True)  # 淡入淡出效果
        5  # 显示5秒
        "mod_assets/location/dormitory/deco/d25/garland_on_2.png" with Dissolve(3, alpha=True)  # 淡入淡出效果
        5  # 显示5秒
        repeat  # 循环播放

# 圣诞树装饰 - 根据时间和动画设置切换不同状态
image dormitory_d25_tree = ConditionSwitch(
    "mas_isNightNow()", ConditionSwitch(  # 如果是夜晚
        "persistent._mas_disable_animations", "mod_assets/location/dormitory/deco/d25/tree_lights_on_1.png",  # 如果禁用动画，使用静态圣诞树
        "not persistent._mas_disable_animations", "dormitory_d25_night_tree_lights_atl"  # 否则使用动画圣诞树
    ),
    "True", MASFilterSwitch(  # 白天时圣诞树灯光关闭
        "mod_assets/location/dormitory/deco/d25/tree_lights_off.png"
    )
)

# 圣诞节夜晚圣诞树灯光动画
image dormitory_d25_night_tree_lights_atl:
    block:
        "mod_assets/location/dormitory/deco/d25/tree_lights_on_1.png"  # 第一帧灯光
        1.5  # 显示1.5秒
        "mod_assets/location/dormitory/deco/d25/tree_lights_on_2.png"  # 第二帧灯光
        1.5  # 显示1.5秒
        "mod_assets/location/dormitory/deco/d25/tree_lights_on_3.png"  # 第三帧灯光
        1.5  # 显示1.5秒
    repeat  # 循环播放

# 圣诞礼物堆 - 根据已送礼物数量显示不同状态
image dormitory_d25_gifts = ConditionSwitch(
    "len(persistent._mas_d25_gifts_given) == 0", "mod_assets/location/dormitory/deco/d25/gifts_0.png",  # 没有礼物
    "0 < len(persistent._mas_d25_gifts_given) < 3", "dormitory_d25_gifts_1",  # 1-2个礼物
    "3 <= len(persistent._mas_d25_gifts_given) <= 4", "dormitory_d25_gifts_2",  # 3-4个礼物
    "True", "dormitory_d25_gifts_3"  # 5个及以上礼物
)

# 1-2个礼物的图像
image dormitory_d25_gifts_1 = MASFilterSwitch(
    "mod_assets/location/dormitory/deco/d25/gifts_1.png"
)

# 3-4个礼物的图像
image dormitory_d25_gifts_2 = MASFilterSwitch(
    "mod_assets/location/dormitory/deco/d25/gifts_2.png"
)

# 5个及以上礼物的图像
image dormitory_d25_gifts_3 = MASFilterSwitch(
    "mod_assets/location/dormitory/deco/d25/gifts_3.png"
)

#======================================================================
# 装饰物注册到MAS系统
# 此部分将所有定义的装饰物注册到MAS中，使其能够在游戏中正确显示
#======================================================================
init 501 python:
    # 注册万圣节天花板灯光
    MASImageTagDecoDefinition.register_img(
        "mas_o31_ceiling_lights",
        submod_background_dormitory.background_id,
        MASAdvancedDecoFrame(zorder=5),  # 设置图层顺序
        replace_tag="dormitory_o31_ceiling_lights"
    )

    # 注册万圣节墙上蜡烛
    MASImageTagDecoDefinition.register_img(
        "mas_o31_wall_candle",
        submod_background_dormitory.background_id,
        MASAdvancedDecoFrame(zorder=4),  # 设置图层顺序
        replace_tag="dormitory_o31_wall_candle"
    )

    # 注册万圣节猫框架动画
    MASImageTagDecoDefinition.register_img(
        "mas_o31_cat_frame",
        submod_background_dormitory.background_id,
        MASAdvancedDecoFrame(zorder=4),  # 设置图层顺序
        replace_tag="dormitory_o31_cat_frame"
    )

    # 注册万圣节墙上蝙蝠
    MASImageTagDecoDefinition.register_img(
        "mas_o31_wall_bats",
        submod_background_dormitory.background_id,
        MASAdvancedDecoFrame(zorder=4),  # 设置图层顺序
        replace_tag="dormitory_o31_wall_bats"
    )

    # 注册万圣节窗户幽灵
    MASImageTagDecoDefinition.register_img(
        "mas_o31_window_ghost",
        submod_background_dormitory.background_id,
        MASAdvancedDecoFrame(zorder=4),  # 设置图层顺序
        replace_tag="dormitory_o31_window_ghost"
    )

    # 注册万圣节蜘蛛网
    MASImageTagDecoDefinition.register_img(
        "mas_o31_cobwebs",
        submod_background_dormitory.background_id,
        MASAdvancedDecoFrame(zorder=4),  # 设置图层顺序
        replace_tag="dormitory_o31_cobwebs"
    )

    # 注册万圣节蜡烛
    MASImageTagDecoDefinition.register_img(
        "mas_o31_candles",
        submod_background_dormitory.background_id,
        MASAdvancedDecoFrame(zorder=5),  # 设置图层顺序
        replace_tag="o31_candles"
    )

    # 注册万圣节南瓜灯
    MASImageTagDecoDefinition.register_img(
        "mas_o31_jack_o_lantern",
        submod_background_dormitory.background_id,
        MASAdvancedDecoFrame(zorder=5),  # 设置图层顺序
        replace_tag="dormitory_o31_jack_o_lantern"
    )

    # 注册万圣节花环
    MASImageTagDecoDefinition.register_img(
        "mas_o31_garlands",
        submod_background_dormitory.background_id,
        MASAdvancedDecoFrame(zorder=5),  # 设置图层顺序
        replace_tag="dormitory_o31_garlands"
    )

    # 注册万圣节天花板装饰
    MASImageTagDecoDefinition.register_img(
        "mas_o31_ceiling_deco",
        submod_background_dormitory.background_id,
        MASAdvancedDecoFrame(zorder=6),  # 设置图层顺序
        replace_tag="dormitory_ceiling_deco"
    )

    # 注册万圣节渐晕效果
    MASImageTagDecoDefinition.register_img(
        "mas_o31_vignette",
        submod_background_dormitory.background_id,
        MASAdvancedDecoFrame(zorder=21),  # 设置图层顺序（较高，覆盖在其他元素上）
        replace_tag="dormitory_o31_vignette"
    )

    # 注册圣诞节横幅
    MASImageTagDecoDefinition.register_img(
        "mas_d25_banners",
        submod_background_dormitory.background_id,
        MASAdvancedDecoFrame(zorder=5),  # 设置图层顺序
        replace_tag="dormitory_d25_banners"
    )

    # 注册圣诞节挂幅
    MASImageTagDecoDefinition.register_img(
        "mas_d25_garlands",
        submod_background_dormitory.background_id,
        MASAdvancedDecoFrame(zorder=5),  # 设置图层顺序
        replace_tag="dormitory_d25_garlands"
    )

    # 注册圣诞树
    MASImageTagDecoDefinition.register_img(
        "mas_d25_tree",
        submod_background_dormitory.background_id,
        MASAdvancedDecoFrame(zorder=6),  # 设置图层顺序
        replace_tag="dormitory_d25_tree"
    )

    # 注册圣诞礼物
    MASImageTagDecoDefinition.register_img(
        "mas_d25_gifts",
        submod_background_dormitory.background_id,
        MASAdvancedDecoFrame(zorder=7),  # 设置图层顺序
        replace_tag="dormitory_d25_gifts"
    )

    # 注册圣诞节灯光
    MASImageTagDecoDefinition.register_img(
        "mas_d25_lights",
        submod_background_dormitory.background_id,
        MASAdvancedDecoFrame(zorder=5),  # 设置图层顺序
        replace_tag="dormitory_d25_lights"
    )

##############################主体部分##################################





#======================================================================
# 生日装饰测试代码
# 注意：此部分目前不可用，需要进一步开发和测试，不可使用
#======================================================================
# init 501 python:
#     from renpy.exports import image as reg_image   # 官方注册接口
# 
#     # 1. 蛋糕（Monika）
#     reg_image(
#         "mas_bday_cake_monika",
#         ConditionSwitch(
#             "store.mas_current_background.background_id == 'submod_dormitory'",
#                 LiveComposite(
#                     (1280, 850),
#                     (0, 0), MASFilterSwitch("mod_assets/location/dormitory/deco/bday/monika_birthday_cake.png"),
#                     (0, 0), ConditionSwitch(
#                         "mas_bday_cake_lit",
#                         "mod_assets/location/dormitory/deco/bday/monika_birthday_cake_lights.png",
#                         "True", Null()
#                     )
#                 ),
#             "True",
#                 LiveComposite(
#                     (1280, 850),
#                     (0, 0), MASFilterSwitch("mod_assets/location/spaceroom/bday/monika_birthday_cake.png"),
#                     (0, 0), ConditionSwitch(
#                         "mas_bday_cake_lit",
#                         "mod_assets/location/spaceroom/bday/monika_birthday_cake_lights.png",
#                         "True", Null()
#                     )
#                 )
#         )
#     )
# 
#     # 2. 蛋糕（玩家）
#     reg_image(
#         "mas_bday_cake_player",
#         ConditionSwitch(
#             "store.mas_current_background.background_id == 'submod_dormitory'",
#                 LiveComposite(
#                     (1280, 850),
#                     (0, 0), MASFilterSwitch("mod_assets/location/dormitory/deco/bday/player_birthday_cake.png"),
#                     (0, 0), ConditionSwitch(
#                         "mas_bday_cake_lit",
#                         "mod_assets/location/dormitory/deco/bday/player_birthday_cake_lights.png",
#                         "True", Null()
#                     )
#                 ),
#             "True",
#                 LiveComposite(
#                     (1280, 850),
#                     (0, 0), MASFilterSwitch("mod_assets/location/spaceroom/bday/player_birthday_cake.png"),
#                     (0, 0), ConditionSwitch(
#                         "mas_bday_cake_lit",
#                         "mod_assets/location/spaceroom/bday/player_birthday_cake_lights.png",
#                         "True", Null()
#                     )
#                 )
#         )
#     )
# 
#     # 3. 横幅
#     reg_image(
#         "mas_bday_banners",
#         ConditionSwitch(
#             "store.mas_current_background.background_id == 'submod_dormitory'",
#                 MASFilterSwitch("mod_assets/location/dormitory/deco/bday/birthday_decorations.png"),
#             "True",
#                 MASFilterSwitch("mod_assets/location/spaceroom/bday/birthday_decorations.png")
#         )
#     )
# 
#     # 4. 气球
#     reg_image(
#         "mas_bday_balloons",
#         ConditionSwitch(
#             "store.mas_current_background.background_id == 'submod_dormitory'",
#                 MASFilterSwitch("mod_assets/location/dormitory/deco/bday/birthday_decorations_balloons.png"),
#             "True",
#                 MASFilterSwitch("mod_assets/location/spaceroom/bday/birthday_decorations_balloons.png")
#         )
#     )
# 
# image dormitory_bday_cake_monika = LiveComposite(
#     (1280, 850),
#     (0, 0), MASFilterSwitch("mod_assets/location/dormitory/deco/bday/monika_birthday_cake.png"),
#     (0, 0), ConditionSwitch(
#         "mas_bday_cake_lit", "mod_assets/location/dormitory/deco/bday/monika_birthday_cake_lights.png",
#         "True", Null()
#         )
# )
# 
# image dormitory_bday_cake_player = LiveComposite(
#     (1280, 850),
#     (0, 0), MASFilterSwitch("mod_assets/location/dormitory/deco/bday/player_birthday_cake.png"),
#     (0, 0), ConditionSwitch(
#         "mas_bday_cake_lit", "mod_assets/location/dormitory/deco/bday/player_birthday_cake_lights.png",
#         "True", Null()
#         )
# )
# 
# image dormitory_bday_banners = MASFilterSwitch(
#     "mod_assets/location/dormitory/deco/bday/birthday_decorations.png"
# )
# 
# image dormitory_bday_balloons = MASFilterSwitch(
#     "mod_assets/location/dormitory/deco/bday/birthday_decorations_balloons.png"
# )

