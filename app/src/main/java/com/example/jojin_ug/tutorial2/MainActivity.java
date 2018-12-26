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
        int n1 = Integer.parseInt(mNumber1.getText().toString());
        int n2 = Integer.parseInt(mNumber2.getText().toString());
        mResultView.setText(Integer.toString(n1 + n2));
    }

    public void subtrackClick(View v) {
        int n1 = Integer.parseInt(mNumber1.getText().toString());
        int n2 = Integer.parseInt(mNumber2.getText().toString());
        mResultView.setText(Integer.toString(n1 - n2));
    }

    public void multiplyClick(View v) {
        int n1 = Integer.parseInt(mNumber1.getText().toString());
        int n2 = Integer.parseInt(mNumber2.getText().toString());
        mResultView.setText(Integer.toString(n1 * n2));
    }

    public void divideClick(View v) {
        int n1 = Integer.parseInt(mNumber1.getText().toString());
        int n2 = Integer.parseInt(mNumber2.getText().toString());
        mResultView.setText(Integer.toString(n1 / n2));
    }
}
