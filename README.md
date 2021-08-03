# Intelligent-Dispatch-in-PowerStation
数学模型:
在进行水能计算与机组选型方案比较时，模型和算法要符合一致性要求，即各方案都应在自身取得最优的条件下与其他方案进行比较，通俗的说法是“优中选优”。因此，水能计算与机组选型的数学模型应内赋三个成分：①给定的径流和给定的机组参数，如何分配各台机组的流量（出力），以使水能充分利用。②对于给定的径流如何选择机组参数与流量分配，使实时发电量最大。③对计及年际变化的长序列水文过程，选择何种机型及相应的“不变量”参数，使多年平均发电量最大。从动态模拟法的基本原理来看，上述三个成分是不可分割的，应统一在一个数学模型中。经验表明，处理上述问题的有效工具是动态规划DP个神经网络NN算法，由此不难得数学模型如下：
![image](https://github.com/ShouqingChen1/Dynamic-Simulation-Method-for-Hydropower-Station-Water-Energy-Calculation-and-Unit-Selection/blob/master/ImagesFolderforReadme/%E9%9D%9E%E7%BA%BF%E6%80%A7%E8%A7%84%E5%88%92%E6%96%B9%E7%A8%8B.png)
 
式中：  为第i台水轮机直径； 为第i台机组出力； 为水头； 为导叶开度； 为桨叶开度； 为单位流量； 为单位转速； 为第i台水轮机转速； 为水轮机效率； 为第i台水轮机的引用流量； 为发电机效率； 为吸出高度； 为发电可用流量； 为模型综合特性曲线运行区域。
模型限制条件中：
第1式为水轮发电机出力公式；第2、3式为水轮机几何相似变换；第4式表示机组出力限制；第5式表示水头限制；第6、7式表示导叶和桨叶开度限制；第8式表示吸出高度限制[2]；第10式表示机组运行工况须在模型曲线范围内；第9式表示机组引用流量不超过最大可用流量。
求解算法:
上述数学模型为非线性规划模型，本文采用神经网络及动态规划算法工具对模型进行求解。
动态规划基本方程为[3]：
 ![image](https://github.com/ShouqingChen1/Dynamic-Simulation-Method-for-Hydropower-Station-Water-Energy-Calculation-and-Unit-Selection/blob/master/ImagesFolderforReadme/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E5%9F%BA%E6%9C%AC%E6%96%B9%E7%A8%8B.png)
式中opt根据模型取max， 表示阶段![image](https://github.com/ShouqingChen1/Dynamic-Simulation-Method-for-Hydropower-Station-Water-Energy-Calculation-and-Unit-Selection/blob/master/ImagesFolderforReadme/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E5%9F%BA%E6%9C%AC%E6%96%B9%E7%A8%8B.png)变量，即第 台水轮机； 表示 阶段状态变量，即 阶段剩余发电可引用流量； 表示第 阶段的初始状态为 ，从 阶段到M阶段所得到的最大值； 表示第 阶段处于状态 时的决策变量，即第 台水轮机的引用流量； 表示状态转移方程， 表示第 阶段的阶段指标，即第 台水轮机的功率。 由状态 所确定的第 阶段的允许决策集合。
