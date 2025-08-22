package com.YALI.Strategy;

/*
 * 2025/7/20
 * Writer:wzx
 * */

public class Client {
    public static void main(String[] args) {
        Context context = new Context(new ConcreteStrategyA());
        context.ContextInterface();
        context = new Context(new ConcreteStrategyB());
        context.ContextInterface();
        context = new Context(new ConcreteStrategyC());
        context.ContextInterface();
        // 由于实例化不同的策略，所以最终在调用context.ContextInterface()的时候，所获得结果就不尽相同
    }
}
