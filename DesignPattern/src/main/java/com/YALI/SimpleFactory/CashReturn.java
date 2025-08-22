package com.YALI.SimpleFactory;

/*
 * 2025/7/20
 * Writer:wzx
 * */
// 返利收费子类
public class CashReturn extends CashSuper{
    private double moneyCondition =  0.0d; // 返利条件
    private double moneyReturn = 0.0d; // 达到返利条件后返回的金额

    public CashReturn(String moneyCondition, String moneyReturn){
        this.moneyCondition = Double.parseDouble(moneyCondition);
        this.moneyReturn = Double.parseDouble(moneyReturn);
    }
    @Override
    public double acceptCash(double money) {
        double result = money;
        if(money >= moneyCondition){
            // Math.floor() 函数返回小于等于参数的最接近的整数。
            result = money - Math.floor(money/moneyCondition)*moneyReturn;
        }
        return result;
    }
}
