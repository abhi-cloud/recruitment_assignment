package com.example.myfirst;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button second = (Button) findViewById(R.id.button1);
        second.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                EditText et = (EditText) findViewById(R.id.getName);
                String name = et.getText().toString();

                Intent start = new Intent(getApplicationContext(), displayName.class);
                start.putExtra("com.example.myfst.SOMETHING", "Hello! " + name);
                startActivity(start);
            }
        });

        Button googleBtn = (Button) findViewById(R.id.button2);

        googleBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String  s = "https://www.google.com";
                Uri webaddress = Uri.parse(s);
                Intent g = new Intent(Intent.ACTION_VIEW, webaddress);

                if(g.resolveActivity(getPackageManager()) != null){
                    startActivity(g);
                }
            }
        });

        Button booked_interface = (Button) findViewById(R.id.booked_button);

        booked_interface.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(getApplicationContext(), Booked.class);
                startActivity(i);
            }
        });

    }
}
