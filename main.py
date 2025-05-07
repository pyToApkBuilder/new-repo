from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog


class BMICalculator(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        self.screen = MDScreen()

        self.height_input = MDTextField(
            hint_text="Height (cm)",
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            size_hint_x=0.8,
            mode="rectangle"
        )
        self.weight_input = MDTextField(
            hint_text="Weight (kg)",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            size_hint_x=0.8,
            mode="rectangle"
        )
        self.result_label = MDLabel(
            text="Healthy BMI range: 18.5 - 24.9",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.50},
            theme_text_color="Hint",
            font_style = "H6"
        )
        self.category_label = MDLabel(
            text="",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.45},
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style = "H5"
        )
        self.calculate_btn = MDRaisedButton(
            text="Calculate BMI",
            pos_hint={"center_x": 0.5, "center_y": 0.62},
            on_release=self.calculate_bmi
        )

        self.screen.add_widget(self.height_input)
        self.screen.add_widget(self.weight_input)
        self.screen.add_widget(self.calculate_btn)
        self.screen.add_widget(self.result_label)
        self.screen.add_widget(self.category_label)

        return self.screen

    def calculate_bmi(self, instance):
        try:
            weight = float(self.weight_input.text)
            height_cm = float(self.height_input.text)
            height_m = height_cm / 100
            bmi = weight / (height_m ** 2)
            upper = (height_m ** 2) * 24.9
            lower = (height_m ** 2) * 18.5
            category, color, range_text = self.get_bmi_category(bmi)

            self.result_label.text = f"BMI: {bmi:.2f} ({range_text})"
            self.category_label.text = f"Category: {category}\nShould be between {lower:.1f} and {upper:.1f}"
            self.category_label.text_color = color
        except ValueError:
            MDDialog(title="Input Error", text="Please enter valid numbers.").open()

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            color = (1, 0.6, 0, 1) if bmi > 16 else (1, 0, 0, 1)
            return "Underweight", color, "Below 18.5"
        elif bmi < 24.9:
            return "Normal weight", (0, 1, 0, 1), "18.6 to 24.9"
        elif bmi < 29.9:
            return "Overweight", (1, 0.6, 0, 1), "25.0 to 29.9"
        else:
            return "Obese", (1, 0, 0, 1), "30 or higher"

if __name__ == '__main__':
    BMICalculator().run()
