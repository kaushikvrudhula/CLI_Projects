package com.example;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By.ByClassName;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
// artdeco-button--secondary
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

import javax.xml.xpath.XPath;

import static java.lang.Thread.sleep;

public class Yo {
    public static void main(String[] args) {

        String links = "https://www.linkedin.com/mynetwork/invitation-manager/";
        WebDriverManager.chromedriver().setup();
        ChromeOptions options = new ChromeOptions();
        options.addArguments("user-data-dir={}\\driver_data".format(System.getProperty("user.dir")));
        WebDriver driver = new ChromeDriver(options = options);
        driver.get("https://linkedin.com");
        while (!new Scanner(System.in).next().equals("1")) {
            System.out.println("press 1 when signed in: ");
        }
        try {
            System.out.println("processing link");
            ;
            driver.get(links);
            sleep(2000);
            WebElement el = driver.findElement(By.xpath(
                    "//button[@class = 'invitation-card__action-btn artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']"));
            el.click();
            System.out.println("Invite Accepted");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}