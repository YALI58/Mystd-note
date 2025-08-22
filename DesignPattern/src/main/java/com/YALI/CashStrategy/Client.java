package com.YALI.CashStrategy;

/*
 * 2025/7/20
 * Writer:wzx
 * */


public class Client {
    public static void main(String[] args) {
        double money = 1000;
        Context context = new Context("正常收费");
        System.out.println(context.getResult(money));
    }
}
