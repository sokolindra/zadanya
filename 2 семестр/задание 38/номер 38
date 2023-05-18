import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите текст:");
        String text = scanner.nextLine();
        String[] words = text.split(" ");
        StringBuilder result = new StringBuilder();
        for (String word : words) {
            if (word.length() > 1) {
                result.append(word.substring(1)).append(word.charAt(0)).append("ауч ");
            } else {
                result.append(word).append("ауч ");
            }
        }
        System.out.println("Результат:");
        System.out.println(result.toString().trim());
    }
}
