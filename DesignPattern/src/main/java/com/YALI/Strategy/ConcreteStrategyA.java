package com.YALI.Strategy;

/*
 * 2025/7/20
 * Writer:wzx
 * */
// 封装了具体的算法或行为，继承与Strategy
// 具体算法A
public class ConcreteStrategyA extends Strategy{

    @Override
    public void AlgorithmInterface() {
        System.out.println("算法A实现");
    }
}
