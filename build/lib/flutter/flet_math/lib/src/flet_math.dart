import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:flutter_math_fork/flutter_math.dart';

class FletMathControl extends StatelessWidget {
  final Control control;
  final Control? parent;
  final List<Control> children;
  final FletControlBackend backend;

  const FletMathControl({
    Key? key,
    required this.backend,
    required this.control,
    required this.children,
    this.parent,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Get properties from control
    String? tex = control.attrString("tex", "");
    Color? textColor = control.attrColor("textColor", context);
    double? fontSize = control.attrDouble("textSize");
    String? fontFamily = control.attrString("fontFamily");
    FontWeight? fontWeight = parseFontWeight(control.attrString("fontWeight"));
    CrossAxisAlignment? crossAxisAlignment = 
        parseCrossAxisAlignment(control.attrString("crossAxisAlignment"));
    MainAxisAlignment? mainAxisAlignment = 
        parseMainAxisAlignment(control.attrString("mainAxisAlignment"));

    // Create text style
    TextStyle textStyle = TextStyle(
      color: textColor,
      fontSize: fontSize,
      fontFamily: fontFamily,
      fontWeight: fontWeight,
    );

    // Create the Math widget
    Widget mathWidget = Math.tex(
      tex ?? "",
      textStyle: textStyle,
    );

    // Wrap with alignment if needed
    if (crossAxisAlignment != null || mainAxisAlignment != null) {
      mathWidget = Column(
        crossAxisAlignment: crossAxisAlignment ?? CrossAxisAlignment.center,
        mainAxisAlignment: mainAxisAlignment ?? MainAxisAlignment.center,
        mainAxisSize: MainAxisSize.min,
        children: [mathWidget],
      );
    }

    // Return constrained control
    return constrainedControl(context, mathWidget, parent, control);
  }
}

FontWeight? parseFontWeight(String? weight) {
  if (weight == null) return null;
  switch (weight.toLowerCase()) {
    case "thin":
      return FontWeight.w100;
    case "extralight":
      return FontWeight.w200;
    case "light":
      return FontWeight.w300;
    case "normal":
      return FontWeight.w400;
    case "medium":
      return FontWeight.w500;
    case "semibold":
      return FontWeight.w600;
    case "bold":
      return FontWeight.w700;
    case "extrabold":
      return FontWeight.w800;
    case "black":
      return FontWeight.w900;
    default:
      return null;
  }
}