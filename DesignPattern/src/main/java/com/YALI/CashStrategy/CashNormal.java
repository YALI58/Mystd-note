package com.YALI.CashStrategy;


/*
 * 2025/7/20
 * Writer:wzx
 * */
// 正常收费子类
public class CashNormal extends CashSuper {

    @Override
    public double acceptCash(double money) {
        return money;
    }
}
