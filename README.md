<<<<<<< HEAD
# MAS--_-
=======
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
# 2. 修改下配置和图像路径
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
#最简单快捷的方法只需要修改标签和路径即可
>>>>>>> db97f4f (9-5)
