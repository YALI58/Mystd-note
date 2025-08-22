package com.YALI.SimpleFactory;

/*
 * 2025/7/20
 * Writer:wzx
 * */


public class CashFactory {

    public CashSuper createCashAccept(String type)
    {
        CashSuper cs = null;
        switch (type){
            case "正常收费":
                cs = new CashNormal();
                break;
            case "满300返100":
                cs = new CashReturn("300","100");
                break;
            case "打8折":
                cs = new CashRebate("0.8");
                break;
        }
        return  cs;
    }
}
