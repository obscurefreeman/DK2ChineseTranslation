# 破门而入2 简体中文模组

作者：[晦涩弗里曼](https://space.bilibili.com/523837807)

更新日期：2025.1.30

<p align="center">
    <div align="center">
        <a href="https://space.bilibili.com/523837807"><img src="https://bilistats.lonelyion.com/followers?uid=523837807&style=for-the-badge" alt="Bilibili"></a>
        <a href="https://discord.gg/zbX7nQa8xF"><img src="https://img.shields.io/badge/Discord-7289DA.svg?logo=discord&logoColor=white&style=for-the-badge" alt="Discord"></a>
        <a href="https://steamcommunity.com/id/obscurefreeman/"><img src="https://img.shields.io/badge/Steam-000000.svg?logo=steam&logoColor=white&style=for-the-badge" alt="Steam"></a>
        <a href="https://www.youtube.com/channel/UCw_S5zgJ6ikGSXtFeAvVK8Q"><img src="https://img.shields.io/badge/Youtube-FF0000?logo=youtube&logoColor=white&style=for-the-badge" alt="Youtube"></a>
        <a href="https://github.com/obscurefreeman"><img src="https://img.shields.io/badge/Github-100000.svg?logo=github&logoColor=white&style=for-the-badge" alt="Github"></a>
    </div>
</p>
<a href="https://imgur.com/UXZtPpy"><img src="https://i.imgur.com/UXZtPpy.png" title="source: imgur.com" /></a>

> 游戏内文本较多的部分（如简报和枪械介绍）可能有疏漏，请随时前往该项目的[Github页面](https://github.com/obscurefreeman/DK2ChineseTranslation)进行修改。

## 安装方式

1. 将模组文件夹放入`DoorKickers2/mods`
2. 打开游戏，进入模组界面
3. 勾选这个模组并重启游戏

## 修改汉化文本

**中文字符在游戏内的自动换行有问题**，因此我写了一个**python脚本**来为部分文件添加换行符，此脚本为`src/linebreaks.py`。若要修改`game.txt`和`briefings.txt`里的本地化文本，请前往`src/localization`文件夹进行修改，然后运行脚本，它会将`src/localization`文件夹里的文件自动加上换行符后替换`localization`文件夹里的文件。
