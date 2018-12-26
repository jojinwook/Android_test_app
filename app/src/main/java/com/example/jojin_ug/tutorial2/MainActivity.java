package com.example.jojin_ug.tutorial2;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private EditText mNumber1;
    private EditText mNumber2;
    private TextView mResultView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mNumber1 = findViewById(R.id.number1);
        mNumber2 = findViewById(R.id.number2);
        mResultView = findViewById(R.id.result);
    }

    public void addClick(View v) {
        setResult("add");
    }

    public void subtrackClick(View v) {
        setResult("subtrack");
    }

    public void multiplyClick(View v) {
        setResult("multiply");
    }

    public void divideClick(View v) {
        setResult("divide");
    }

    private void setResult(String type) {
        int n1 = Integer.parseInt(mNumber1.getText().toString());
        int n2 = Integer.parseInt(mNumber2.getText().toString());
        switch (type) {
            case "add":
                mResultView.setText(Integer.toString(n1 + n2));
                break;
            case "subtrack":
                mResultView.setText(Integer.toString(n1 - n2));
                break;
            case "multiply":
                mResultView.setText(Integer.toString(n1 * n2));
                break;
            case "divide":
                mResultView.setText(Integer.toString(n1 / n2));
                break;
            default:
                mResultView.setText("정확한 연산자를 선택하세요.");
        }
    }
}
