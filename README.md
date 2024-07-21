# 对不同jdk在MC上的性能表现的测试!!

测试 Purpur 1.21 Latest 在不同 Java 21 JDK 的性能表现

## 参赛选手

* Azul Zing
* Azul Zulu
* GraalVM EE
* Adoptium Temurin
* Bellsoft
* Microsoft
* Oracle
* OpenJDK
* IBM OpenJ9
* RedHat
* Amazon Corretto
* Sapmachine
* Huawei Bisheng
* Dragonwell
* Jetbrains Runtime

如果有其他的jdk没有列出来，可以跟我们联系

## JVM参数

所有jdk保持默认的启动参数，不会进行任何的优化，以确保结果的公平性

## 测试项目

### Chunky 预加载

Chunky 预加载主世界半径5000格,比较 TPS,MSPT,CPS,生成时间，内存占用，同时，提供每个jdk对应的spark

目前我们只有此计划，如果您希望测试其他的项目，请提供相应的自动化测试工具(不要指望我去给你写）

## 支持我们

您可以选择以下方式来为这场大型测试提供帮助

### 机器

要求为4h8g以上,拥有80 GB以上的空余空间，操作系统为 Linux

### 自动化测试工具

你可以提供对应项目的自动化测试工具，比如实体，红石，漏斗，这可以让我们的测试更加准确
