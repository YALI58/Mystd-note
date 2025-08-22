package com.YALI.CashStrategy;

/*
 * 2025/7/20
 * Writer:wzx
 * */

public class Context {
    CashSuper cs = null;
    public double getResult(double money) {
        return cs.acceptCash(money);
    }
    // 把实例化具体策略的过程由客户端转移到Context类中，简单工厂的应用
    public Context (String type) {
        switch (type){
            case "正常收费":
                cs= new CashNormal();
                break;
            case "满300返100":
                cs = new CashReturn("300","100");
                break;
            case "打8折":
                cs = new CashRebate("0.8");
                break;
        }
    }
}
