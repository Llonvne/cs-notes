# **Premature Optimization**

*Premature optimization is the root of all evil
过早优化是万恶之源* -- [DonaldKnuth](http://wiki.c2.com/?DonaldKnuth) 唐纳德·克努斯

在Donald Knuth的论文《使用GoTo语句进行结构化编程》中，他写道：“程序员在思考或担心程序的非关键部分的速度上浪费了大量时间，而这些对效率的努力实际上在调试和维护时产生了强烈的负面影响。我们应该忘记小的效率问题，大约有97%的时间：过早优化是万恶之源。然而，在关键的3%中，我们不应该错过机会。”然而，过早优化可以被定义为在我们知道需要优化之前进行优化。

Optimizing up front is often regarded as breaking [YouArentGonnaNeedIt](http://wiki.c2.com/?YouArentGonnaNeedIt)(YAGNI). But by the time we decide that we need to optimize, we might be too close to [UniformlySlowCode](http://wiki.c2.com/?UniformlySlowCode) to [OptimizeLater](http://wiki.c2.com/?OptimizeLater). We can use [PrematureOptimization](http://wiki.c2.com/?PrematureOptimization) as a [RiskMitigation](http://wiki.c2.com/?RiskMitigation) strategy to push back the point of [UniformlySlowCode](http://wiki.c2.com/?UniformlySlowCode), and lower our exposure to the risk of [UniformlySlowCode](http://wiki.c2.com/?UniformlySlowCode) preventing us from reaching our performance target with [OptimizeLater](http://wiki.c2.com/?OptimizeLater).
优化前端通常被认为是违反“你不会需要它”（YAGNI）原则。但是当我们决定需要优化时，我们可能已经接近了“统一缓慢代码”（UniformlySlowCode），无法再推迟优化。我们可以使用“过早优化”作为一种风险缓解策略，将“统一缓慢代码”的出现时间推迟，降低我们在后续优化中无法达到性能目标的风险。

