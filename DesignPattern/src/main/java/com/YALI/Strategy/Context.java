package com.YALI.Strategy;

/*
 * 2025/7/20
 * Writer:wzx
 * */

public class Context {
    Strategy strategy;
    public Context(Strategy strategy){
        this.strategy = strategy;
    }
    //上下文接口
    //根据具体的策略对象，调用其算法的方法
    public void ContextInterface(){
        strategy.AlgorithmInterface();
    }
}
