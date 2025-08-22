package com.YALI.SimpleFactory;

/*
 * 2025/7/20
 * Writer:wzx
 * */

public class Client {
    public static void main(String[] args) {
        double money = 1000;
        CashFactory cashFactory = new CashFactory();
        CashSuper cashSuper = cashFactory.createCashAccept("正常收费");
        System.out.println(cashSuper.acceptCash(money));
    }
}
