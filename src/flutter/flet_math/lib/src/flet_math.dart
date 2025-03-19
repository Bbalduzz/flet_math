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
    bool selectable = control.attrBool("selectable", false) ?? false;
    
    // Create text style
    TextStyle textStyle = TextStyle(
      color: textColor,
      fontSize: fontSize,
      fontFamily: fontFamily,
      fontWeight: fontWeight,
    );

    // Create the Math widget
    Widget mathWidget;
    if (selectable) {
      mathWidget = SelectableMath.tex(
        tex ?? "",
        textStyle: textStyle,
      );
    } else {
      mathWidget = Math.tex(
        tex ?? "",
        textStyle: textStyle,
      );
    }

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

CrossAxisAlignment? parseCrossAxisAlignment(String? alignment) {
  if (alignment == null) return null;
  switch (alignment.toLowerCase()) {
    case "start":
      return CrossAxisAlignment.start;
    case "end":
      return CrossAxisAlignment.end;
    case "center":
      return CrossAxisAlignment.center;
    case "stretch":
      return CrossAxisAlignment.stretch;
    case "baseline":
      return CrossAxisAlignment.baseline;
    default:
      return null;
  }
}

MainAxisAlignment? parseMainAxisAlignment(String? alignment) {
  if (alignment == null) return null;
  switch (alignment.toLowerCase()) {
    case "start":
      return MainAxisAlignment.start;
    case "end":
      return MainAxisAlignment.end;
    case "center":
      return MainAxisAlignment.center;
    case "spacearound":
    case "space_around":
      return MainAxisAlignment.spaceAround;
    case "spacebetween":
    case "space_between":
      return MainAxisAlignment.spaceBetween;
    case "spaceevenly":
    case "space_evenly":
      return MainAxisAlignment.spaceEvenly;
    default:
      return null;
  }
}