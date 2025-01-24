# easy-configs-rime

小狼毫输入法设置

# 参考

配置参考： [雾凇拼音](https://github.com/iDvel/rime-ice)

配色参考：[Rime 鼠须管输入法皮肤实验室](https://www.figma.com/community/file/1166934605535869911/rime)，预览图如下：

![Figma截图](./legacy/images/figma.png)

# 主题截图

在 Windows 上，加载 `legacy/weasel.custom.yaml` 配置后的部分主题如下所示：

- 蓝色.暗

![蓝色.暗](./legacy/images/blue-dark.png)

- 蓝色.亮

![蓝色.亮](./legacy/images/blue-light.png)

> P.S. my favorite~

- 深灰.亮（darkgrey-light）

![深灰.亮](./legacy/images/darkgrey-light.png)

- 绿色.亮（green-light）

![绿色.亮](./legacy/images/green-light.png)

- 灰色.亮（grey-light）

![灰色.亮](./legacy/images/grey-light.png)

- MacOS.亮 (macos-light)

![MacOS.亮](./legacy/images/macos.png)

- 粉色.暗（pink-dark）

![粉色.暗](./legacy/images/pink-dark.png)

- 紫色.亮（purple-light）

![紫色.亮](./legacy/images/purple-light.png)

- 黑白.暗（taiji-dark）

![太极.暗](./legacy/images/taiji-dark.png)

- 黑白.亮（taiji-light）

![太极.亮](./legacy/images/taiji-light.png)

- 黄色.暗（yellow-dark）

![黄色.暗](./legacy/images/yellow-dark.png)

# 自定义主题

对于亮色主题，遵循的设计原则：

- 背景色：`#FFFFFF`
- 候选字颜色： `#454545`
- 标签（未选中）颜色： `#8E8E8E`
- 候选字（选中）文字颜色：根据个人喜好选择
- 候选字（选中）背景颜色：`候选字（选中）文字 颜色`不透明度 20%（Alpha 的值约为 38/0x26）
- 标签（选中）颜色：和候选字（选中）文字颜色保持一致

对于暗色主题，遵循的设计原则：

- 背景色：`#000000`
- 候选字颜色： `#454545` 的反色 `#BABABA`
- 标签（未选中）颜色： `#8E8E8E` 的反色 `#717171`
- 候选字（选中）文字颜色：`#000000`
- 候选字（选中）背景颜色：亮色主题中`候选字（选中）背景颜色`
- 标签（选中）颜色：和候选字（选中）文字颜色保持一致

以下是根据 [中国传统色](https://www.zhongguose.com) 和上述设计原则做出来的部分主题的截图（`chinese-colors/weasel.custom.yaml`）：

- 靛青

  ![靛青](./chinese-colors/images/dianqing.png)

- 靛青/暗

  ![靛青/暗](./chinese-colors/images/dianqing_dark.png)

- 高粱红

  ![高粱红](./chinese-colors/images/gaolianghong.png)

- 高粱红/暗

  ![高粱红/暗](./chinese-colors/images/gaolianghong_dark.png)

- 古铜褐

  ![古铜褐](./chinese-colors/images/gutonghe.png)

- 古铜褐/暗

  ![古铜褐/暗](./chinese-colors/images/gutonghe_dark.png)

- 蓝绿

  ![蓝绿](./chinese-colors/images/lanlv.png)

- 蓝绿/暗

  ![蓝绿/暗](./chinese-colors/images/lanlv_dark.png)


- 苋菜红

  ![苋菜红](./chinese-colors/images/xiancaihong.png)

- 苋菜红/暗

  ![苋菜红/暗](./chinese-colors/images/xiancaihong_dark.png)

- 苋菜紫

  ![苋菜紫](./chinese-colors/images/xiancaizi.png)

- 苋菜紫/暗

  ![苋菜紫/暗](./chinese-colors/images/xiancaizi_dark.png)

- 喜蛋红

  ![喜蛋红](./chinese-colors/images/xidanhong.png)

- 喜蛋红/暗

  ![喜蛋红/暗](./chinese-colors/images/xidanhong_dark.png)

# 其他资源

- [传统色](https://colors.masantu.com/#/)

- [Adobe color wheel](https://color.adobe.com/zh/create/color-wheel)

<div style="display: flex; flex-wrap: wrap;">
    <div style="width: 50px; height: 50px; background-color: #8F77B5; margin: 5px; display: flex; align-items: center; justify-content: center;">
        <span style="color: white; font-size: 12px;">紫苑</span>
    </div>
    <div style="width: 50px; height: 50px; background-color: #725338; margin: 5px; display: flex; align-items: center; justify-content: center;">
        <span style="color: white; font-size: 12px;">醤色</span>
    </div>
    <div style="width: 50px; height: 50px; background-color: #25446B; margin: 5px; display: flex; align-items: center; justify-content: center;">
        <span style="color: white; font-size: 12px;">労働布色</span>
    </div>
    <div style="width: 50px; height: 50px; background-color: #F5CEBE; margin: 5px; display: flex; align-items: center; justify-content: center;">
        <span style="color: black; font-size: 12px;">果肉色</span>
    </div>
    <div style="width: 50px; height: 50px; background-color: #F6C555; margin: 5px; display: flex; align-items: center; justify-content: center;">
        <span style="color: white; font-size: 12px;">梔子</span>
    </div>
    <div style="width: 50px; height: 50px; background-color: #FB9966; margin: 5px; display: flex; align-items: center; justify-content: center;">
        <span style="color: white; font-size: 12px;">深支子</span>
    </div>
    <div style="width: 50px; height: 50px; background-color: #3F486C; margin: 5px; display: flex; align-items: center; justify-content: center;">
        <span style="color: white; font-size: 12px;">紺青</span>
    </div>
    <div style="width: 50px; height: 50px; background-color: #D15D5E; margin: 5px; display: flex; align-items: center; justify-content: center;">
        <span style="color: black; font-size: 12px;">銀朱</span>
    </div>
    <div style="width: 50px; height: 50px; background-color: #A71368; margin: 5px; display: flex; align-items: center; justify-content: center;">
        <span style="color: white; font-size: 12px;">品紅</span>
    </div>
    <div style="width: 50px; height: 50px; background-color: #1F3696; margin: 5px; display: flex; align-items: center; justify-content: center;">
        <span style="color: white; font-size: 12px;">宝石藍</span>
    </div>
</div>