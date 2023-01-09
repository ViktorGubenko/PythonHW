import java.io.*;

public class task3 {
    public static void main(String[] args) { // throws Exception {

        try (BufferedReader BufReader = new BufferedReader(new FileReader("TASK_3/file_text.txt"))) {
            StringBuilder strBuild = new StringBuilder();
            String strRead;
            while ((strRead = BufReader.readLine()) != null) {
                strBuild.append(strRead);
            }
            strBuild.deleteCharAt(strBuild.length() - 1)
                    .deleteCharAt(strBuild.length() - 1)
                    .replace(0, 1, "  ");

            String upgradeText = strBuild.toString();

            upgradeText = upgradeText.replace("}", "\n").replace("{", "")
                    .replace("фамилия", "Студент")
                    .replace("оценка", "получил")
                    .replace("предмет", "по предмету")
                    .replace("\"", "")
                    .replace(":", " ")
                    .replace(",", " ");
            try (FileWriter fw = new FileWriter("TASK_3/new_file_text.txt", false)) {
                fw.write(upgradeText);
                System.out.println(upgradeText);
            }
        } catch (IOException ex) {
            System.out.println("erroreeee");
        }
    }
}
