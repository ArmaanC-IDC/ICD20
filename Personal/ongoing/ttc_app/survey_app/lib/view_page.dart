import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class ViewPage extends StatefulWidget {
  static List<String> responses = [];

  const ViewPage({super.key}); // Static list to store responses

  @override
  _ViewPageState createState() => _ViewPageState();
}

class _ViewPageState extends State<ViewPage> {
  @override
  void initState() {
    super.initState();
    loadResponses();
  }

  void loadResponses() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    setState(() {
      ViewPage.responses = prefs.getStringList('responses') ?? [];
    });
  }

  void saveResponses() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    prefs.setStringList('responses', ViewPage.responses);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('View Page'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('Responses:'),
            Expanded(
              child: ListView.builder(
                itemCount: ViewPage.responses.length,
                itemBuilder: (context, index) {
                  return ListTile(
                    title: Text(ViewPage.responses[index]),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    saveResponses(); // Save responses when the widget is disposed
    super.dispose();
  }
}
