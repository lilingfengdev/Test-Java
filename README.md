# 对不同jdk在MC上的性能表现的测试!!

测试 Purpur 1.21 Latest 在不同 Java 21 JDK 的性能表现

## 参赛选手

### Linux

* Azul Zing
* Azul Zulu
* GraalVM EE
* GraalVM CE
* Adoptium Temurin
* Bellsoft
* Microsoft
* Oracle
* OpenJDK
* IBM OpenJ9
* Amazon Corretto
* Sapmachine
* Huawei Bisheng
* Dragonwell
* Jetbrains Runtime
* OpenLogic
* RedHat

### Windows

Java 21:

* Azul Zulu
* GraalVM EE
* GraalVM CE
* Adoptium Temurin
* Bellsoft
* Microsoft
* Oracle
* OpenJDK
* IBM OpenJ9
* Amazon Corretto
* Sapmachine
* Dragonwell
* OpenLogic
* RedHat*

*:(Java 21的 RedHat 由于一些原因没有参赛,但已经补测，不如GraalVM EE)

**[点击查看Java21测试结果 (Windows)](./Windows/Java%2021/Java21.md)**

Java 8:

* Adoptium Eclipse Temurin
* Alibaba Dragonwell
* IBM OpenJ9
* RedHat
* Bellsoft
* Tencent Kona
* Oracle
* Azul Zulu
* Amazon Corretto

**[点击查看Java8测试结果 (Windows)](./Windows/Java%208/Java8.md)**

## JVM参数

所有jdk保持默认的启动参数，不会进行任何的优化，以确保结果的公平性

## 测试项目

### Chunky 预加载

Chunky 预加载主世界半径2500格,比较 TPS,MSPT,CPS,生成时间，内存占用，同时，提供每个jdk对应的spark

目前我们只有此计划，如果您希望测试其他的项目，请提供相应的自动化测试工具(不要指望我去给你写）

## GC (垃圾回收器) 测试

已测试的垃圾回收器:

- G1GC
- Parallel GC
- Serial GC
- Shenandoah GC(IU Mode)
- Shenandoah GC(Normal)
- Shenandoah GC(被动模式)
- ZGC Generational
- ZGC Non-Proactive

**[点击查看GC测试详情](./GC/garbage-collector.md)**

## 支持我们

您可以选择以下方式来为这场大型测试提供帮助

### 机器

要求为4h8g以上,拥有80 GB以上的空余空间，操作系统为 Linux 或 Windows

### 自动化测试工具

你可以提供对应项目的自动化测试工具，比如实体，红石，漏斗，这可以让我们的测试更加准确

## 完成

测试结束后，我们会公开这次测试所有的自动化脚本和Spark Profile,以及图表数据分析

您可以将测试结果以文字视频的方式转发，但请标注本仓库