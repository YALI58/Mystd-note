package com.YALI.SimpleFactory;

/*
 * 2025/7/20
 * Writer:wzx
 * */

public class CashRebate extends CashSuper{
    private double moneyRebate = 1d;
    public CashRebate(String moneyRebate) {
        this.moneyRebate = Double.parseDouble(moneyRebate);
    }

    @Override
    public double acceptCash(double money) {
        return money*moneyRebate;
    }
}
